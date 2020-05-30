from urllib import robotparser


class Checkwebsite:
    def __init__(self, robots_txt_url):
        self.rp = robotparser.RobotFileParser()
        self.rp.set_url(robots_txt_url)
        self.rp.read()

    def Check_url(self,url):
        return self.rp.can_fetch("*",url)

if __name__ =='__main__':
    cw =Checkwebsite('https://www.macrotrends.net/robots.txt')
    Check =cw.Check_url('https://www.macrotrends.net/search/')
    print('can i scrap this website?',Check)