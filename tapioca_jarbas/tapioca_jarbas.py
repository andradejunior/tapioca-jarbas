from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)


from .resource_mapping import RESOURCE_MAPPING


class JarbasClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'http://jarbas.datasciencebr.com/api/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(JarbasClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        return params

    def get_iterator_list(self, response_data):
        return response_data.get('results', response_data)

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        next_url = response_data.get('next', '')
        if not next_url:
            return

        iterator_request_kwargs['url'] = next_url
        return iterator_request_kwargs


Jarbas = generate_wrapper_from_adapter(JarbasClientAdapter)
