# 作者: Michael(phb)
# 2022年06月26日20时52分50秒
class MiniOS:
    def __init__(self, name):
        self.name = name
        self.apps = []

    def __str__(self):
        return f'{self.name} 安装的软件列表为 {self.apps}'

    def install_app(self, app):
        if app.name in self.apps:
            print(f'已经安装了{app.name}，无需再次安装')
        else:
            app.install()
            self.apps.append(app.name)


class App:
    def __init__(self, name, version, desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return f'{self.name}的当前版本是{self.version}-{self.desc}'

    def install(self):
        print(f'将{self.name}[{self.version}]的执行程序复制到程序目录')


class Pycharm(App):
    pass


class Chrome(App):
    def install(self):
        print('正在解压安装程序...')
        super().install()


linux = MiniOS('Linux')
print(linux)

pycharm = Pycharm('Pycharm', '1.0', 'python开发的IDE环境')

chrome = Chrome('Chrome', '2.0', '谷歌浏览器')

linux.install_app(pycharm)
linux.install_app(chrome)
linux.install_app(chrome)

print(linux)
