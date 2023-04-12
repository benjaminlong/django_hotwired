from django.core.paginator import EmptyPage, InvalidPage, Paginator


def pager(queryset, page, items_per_page=10, base_url=""):
    """
    A generic pager built on top of Django core's Paginator.
    https://docs.djangoproject.com/en/dev/topics/pagination/
    Arguments:
        queryset: QuerySet, a queryset object to paginate
        page: int, current page number
        items_per_page: int, number of items per page
        pages_num: int, number of pages to display
        base_url: string, base url use to got list of items TODO: Update comment !
    Returns:
        custom_pager: a django.core.paginator.Page instance with a few additional attributes:
            pages_to_display: list, allow to iterate and create a google-style pager
            display_pager: bool, True if there are more than one page to display
            base_url: string. TODO: Add comment !
    """
    paginator = Paginator(queryset, items_per_page)

    try:
        page = int(page)
    except (ValueError, TypeError):
        page = 1

    total_pages = paginator.num_pages

    try:
        custom_pager = paginator.page(page)
    except (EmptyPage, InvalidPage):
        # If page request is out of range, deliver last page of results.
        custom_pager = paginator.page(total_pages)

    setattr(custom_pager, "base_url", base_url)
    setattr(custom_pager, "display_pager", total_pages > 1)
    return custom_pager
