class UrlBuilder():

    def __init__(self, domain_name, scheme=None, top_level_domain=None):

        self.scheme = scheme
        self.domain_name = domain_name
        self.top_level_domain = top_level_domain

    @property
    def scheme(self):

        return self.__scheme

    @scheme.setter
    def scheme(self, value):

        if value is None:
            self.__scheme = 'https'
        else:
            self.__scheme = value

    @property
    def domain_name(self):

        return self.__domain_name

    @domain_name.setter
    def domain_name(self, value):

        self.__domain_name = value

    @property
    def top_level_domain(self):

        return self.__top_level_domain

    @top_level_domain.setter
    def top_level_domain(self, value):

        if value is None:
            self.__top_level_domain = 'com'
        else:
            self.__top_level_domain = value

    @property
    def domain_url(self):

        return f'{self.scheme}://{self.domain_name}.{self.top_level_domain}'

    def get_url_to_path(self, path):

        return f'{self.domain_url}/{path}'
