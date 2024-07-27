"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from .browsers import chrome, safari, firefox, edge
from .platforms import ios, android, linux, windows, macos
from .. import formats, utils, exceptions


class Generator:
    def __init__(self, device, platform, browser):
        self.device = device
        self.platform = platform
        self.browser = browser

        self.platform_version = self.__platform_version()
        self.browser_version = self.__browser_version()
        self.user_agent = self.__user_agent()

    def __platform_version(self):
        if self.platform == 'windows':
            return windows.get_version()
        elif self.platform == 'macos':
            return macos.get_version()
        elif self.platform == 'ios':
            return ios.get_version()
        elif self.platform == 'linux':
            return linux.get_version()
        elif self.platform == 'android':
            return android.get_version()

    def __browser_version(self):
        if self.browser == 'chrome':
            return chrome.get_version()
        elif self.browser == 'safari':
            return safari.get_version()
        elif self.browser == 'firefox':
            return firefox.get_version()
        elif self.browser == 'edge':
            return edge.get_version()

    def __user_agent(self):
        if self.platform == 'windows':
            if self.browser == 'chrome':
                template = utils.choice((
                    'Mozilla/5.0 (Windows NT {windows}; Win64; x64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
                    'Mozilla/5.0 (Windows NT {windows}; WOW64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}'
                ))
                template = template.replace('{windows}', self.platform_version['major'])
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'edge':
                template = utils.choice((
                    'Mozilla/5.0 (Windows NT {windows}; Win64; x64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit} Edg/{chrome}',
                ))
                template = template.replace('{windows}', self.platform_version['major'])
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'firefox':
                template = utils.choice((
                    'Mozilla/5.0 (Windows NT {windows}; Win64; x64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
                    'Mozilla/5.0 (Windows NT {windows}; WOW64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
                ))
                template = template.replace('{windows}', self.platform_version['major'])
                template = template.replace('{firefox}', formats.version(self.browser_version, strip_zero=True))
                return template

        elif self.platform == 'linux':
            if self.browser == 'chrome':
                template = utils.choice((
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
                    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
                ))
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'edge':
                template = utils.choice((
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit} Edg/{chrome}',
                ))
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'firefox':
                template = utils.choice((
                    'Mozilla/5.0 (X11; Linux x86_64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
                    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
                ))
                template = template.replace('{linux}', self.platform_version['major'])
                template = template.replace('{firefox}', formats.version(self.browser_version, strip_zero=True))
                return template

        elif self.platform == 'android' and self.device == 'mobile':
            if self.browser == 'chrome':
                template = 'Mozilla/5.0 (Linux; Android {android}{model}{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/{webkit}'
                template = template.replace('{android}', self.platform_version['major'].replace('.0', ''))
                if 'platform_model' in self.platform_version and self.platform_version['platform_model']:
                    template = template.replace('{model}', '; ' + self.platform_version['platform_model'])
                if 'build_number' in self.platform_version and self.platform_version['build_number']:
                    template = template.replace('{build}', '; Build/' + self.platform_version['build_number'])
                template = template.replace('{build}', '').replace('{model}', '')
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'edge':
                template = 'Mozilla/5.0 (Linux; Android {android}{model}{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/{webkit} EdgA/{chrome}'
                template = template.replace('{android}', self.platform_version['major'].replace('.0', ''))
                if 'platform_model' in self.platform_version and self.platform_version['platform_model']:
                    template = template.replace('{model}', '; ' + self.platform_version['platform_model'])
                if 'build_number' in self.platform_version and self.platform_version['build_number']:
                    template = template.replace('{build}', '; Build/' + self.platform_version['build_number'])
                template = template.replace('{build}', '').replace('{model}', '')
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'firefox':
                template = 'Mozilla/5.0 (Android {android}; Mobile; rv:{firefox}) Gecko/{firefox} Firefox/{firefox}'
                template = template.replace('{android}', self.platform_version['major'].replace('.0', ''))
                template = template.replace('{firefox}', formats.version(self.browser_version))
                return template

        elif self.platform == 'macos':
            if self.browser == 'chrome':
                template = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}'
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'edge':
                template = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit} Edg/{chrome}'
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'safari':
                template = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari} Safari/{webkit}'
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{safari}', formats.version(self.browser_version))
                return template
            if self.browser == 'firefox':
                template = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:{firefox}) Gecko/20100101 Firefox/{firefox}'
                template = template.replace('{firefox}', formats.version(self.browser_version, strip_zero=True))
                return template

        elif self.platform == 'ios':
            if self.browser == 'chrome':
                template = 'Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) CriOS/{chrome} Mobile/15E148 Safari/{webkit}'
                template = template.replace('{ios}', formats.version(self.platform_version, strip_zero=True).replace('.', '_'))
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'edge':
                template = 'Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/15.0 EdgiOS/{chrome} Mobile/15E148 Safari/{webkit}'
                template = template.replace('{ios}', formats.version(self.platform_version, strip_zero=True).replace('.', '_'))
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'safari':
                template = 'Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari} Mobile/15E148 Safari/{webkit}'
                template = template.replace('{ios}', formats.version(self.platform_version, strip_zero=True).replace('.', '_'))
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{safari}', formats.version(self.browser_version))
                return template
            if self.browser == 'firefox':
                template = 'Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/{firefox} Mobile/15E148 Safari/605.1.15'
                template = template.replace('{ios}', formats.version(self.platform_version, strip_zero=True).replace('.', '_'))
                template = template.replace('{firefox}', formats.version(self.browser_version, strip_zero=True))
                return template

        raise exceptions.CannotGenerateError(self)
