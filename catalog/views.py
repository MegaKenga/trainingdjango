from django.db.models import Q, Prefetch
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib import messages

from catalog.models import Category, Brand, Offer


def breadcrumbs_path(category):
    parents = category.parents.all()
    breadcrumbs = []
    while len(parents) > 0:
        parents_path = [parent for parent in parents if parent.brand is not None]
        if parents_path:
            if len(parents_path) > 1:
                raise ValueError('We don\'t expect multiple brand parents')
            if len(parents_path) == 1:
                breadcrumbs.insert(0, parents_path [0])
            parents = parents_path[0].parents.all()
        else:
            parents_path = [parent for parent in parents if parent.brand is None]
            if len(parents_path) > 1:
                raise ValueError('We don\'t expect multiple brand parents')
            if len(parents_path) == 1:
                breadcrumbs.insert(0, parents_path[0])
            parents = parents_path[0].parents.all()
    return breadcrumbs


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.visible.all().order_by('name')
        context['categories'] = Category.visible.filter(parents=None).filter(brand=None)
        return context


class CategoryView(TemplateView):
    model = Category
    template_name = 'catalog/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.visible.prefetch_related('parents').select_related('brand').get(slug=self.kwargs['category_slug'])
        context['brand'] = category.brand
        context['category'] = category
        context['breadcrumbs'] = breadcrumbs_path(category)
        return context


class BrandView(TemplateView):
    model = Category
    template_name = 'catalog/brand.html'

    def get_queryset(self):
        return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = get_object_or_404(Brand.visible, slug=self.kwargs['brand_slug'])
        context['categories'] = Category.visible.filter(parents=None, brand=brand).select_related('brand')
        context['brand'] = brand
        return context


class OfferView(TemplateView):
    model = Offer
    template_name = 'catalog/offer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category.visible, slug=self.kwargs['category_slug'])
        context['category'] = category
        context['offers'] = Offer.visible.filter(category=category.id).select_related('category')
        context['breadcrumbs'] = breadcrumbs_path(category)
        return context


SEARCH_QUERY_PARAM = 'q'


class SiteSearchView(ListView):
    model = Category
    template_name = 'catalog/search.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get(SEARCH_QUERY_PARAM, '')
        qs = super().get_queryset()
        if len(query) < 3:
            messages.error(self.request, message='Слишком короткий запрос. Попробуйте увеличить количество символов в запросе')
            return qs.none()

        related_offers = Prefetch(
            'offer',
            queryset=Offer.visible.filter(name__icontains=query) or Offer.visible.filter(description__icontains=query),
            to_attr='related_offers')
        qs = (
            qs.filter(is_final=True).filter(Q(name__icontains=query) | Q(offer__name__icontains=query) | Q(offer__description__icontains=query))
            .prefetch_related(related_offers).distinct()
        )
        return qs
