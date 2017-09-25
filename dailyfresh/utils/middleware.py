class UrlPathRecordMiddleware(object):
    """用户访问URL地址记录中间件类"""
    exclude_path = ['/user/login/', '/user/register/', '/user/logout/']

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if request.path not in UrlPathRecordMiddleware.exclude_path and not request.is_ajax():
            # 记录这个地址
            request.session['pre_url_path'] = request.path