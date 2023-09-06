from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class ProductPagination(PageNumberPagination):
    page_size  = 2 #define page size
    page_query_param = 'p' # change the default query param name
    page_size_query_param = 'size' # handle the user so that they can  change the page size
    max_page_size = 4 # limitmax size
    
    
    
class ProductPagination2(LimitOffsetPagination):
    default_limit = 2 # initially set the limit
    limit_query_param = 'my_limit' # change the default param name
    offset_query_param = 'my_start' 
    max_limit = 3 # set the max limit