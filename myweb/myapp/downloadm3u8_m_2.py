import os
import threading

from Crypto.Cipher import AES
import time
import requests  # , _thread


class d_from_url(threading.Thread):
    # ts_name, ts_url, key
    def __init__(self, ts_name, ts_url, key):
        threading.Thread.__init__(self)
        self.ts_name = ts_name  #
        self.ts_url = ts_url
        self.key = key

    def run(self):

        # time.sleep(1)
        # if len(self.ts_name)>16:
        #     self.ts_name = self.ts_name[-16:-1]
        try:
            if os.path.exists(self.ts_name):
                if os.path.getsize(self.ts_name) > 10:
                    print('*' * 20, '--', '文件已存在', self.ts_name, os.path.getsize(self.ts_name), '--', '*' * 20)
                else:
                    if 'ts' in self.ts_url:
                        if len(self.key):  # AES 解密
                            cryptor = AES.new(self.key, AES.MODE_CBC, self.key)
                            # with open(ts_name + ".mp4", 'ab') as f:

                            with open(self.ts_name, 'ab') as f:
                                f.write(cryptor.decrypt(requests.get(self.ts_url).content))
                        else:
                            # with open(ts_name + ".mp4", 'ab') as f:
                            with open(self.ts_name, 'ab') as f:
                                f.write(requests.get(self.ts_url).content)
                                f.flush()
            else:
                if 'ts' in self.ts_url:
                    if len(self.key):  # AES 解密
                        cryptor = AES.new(self.key, AES.MODE_CBC, self.key)
                        # with open(ts_name + ".mp4", 'ab') as f:

                        with open(self.ts_name, 'ab') as f:
                            f.write(cryptor.decrypt(requests.get(self.ts_url).content))
                    else:
                        # with open(ts_name + ".mp4", 'ab') as f:
                        with open(self.ts_name, 'ab') as f:
                            f.write(requests.get(self.ts_url).content)
                            f.flush()
                pass
        except Exception as e:
            print('d_from_url:', e)
            print('正在尝试重新下载', self.ts_url)
            ds = d_from_url(self.ts_name, self.ts_url, self.key)
            ds.start()
            # ds.join()
            pass
        print('*' * 20, '--', self.ts_name, '--', '*' * 20)
        time.sleep(1)
        return 0


def check_empty_file():
    pass


class Downloadm3u8(download_dir="", m3u8url="",merge_or_not=True):
    '''
    download_dir : 指定下载目录 若不指定 默认 z:\\m3u8
    m3u8url      : 视频的 链接
    merge_or_not      : 视频下载完成后是否拼接 默认 拼接
    '''
    def __init__(self,download_dir,m3u8url,merge_or_not):
        self.download_dir = download_dir
        self.m3u8url = m3u8url
        self.merger_or_not = merge_or_not
    def downloadm3u8(self, download_dir='C:\\m3u8', m3u8url=''):
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
            # os.path.join()
        if not m3u8url == '':
            # index.m3u8
            tail = m3u8url.split('/')[-1]
            # https://cdn6-video.wwjingtou.com:8081/20191116/LNe9luPa
            head = m3u8url.replace(tail, '')
            print(head)
            # LNe9luPa
            name = m3u8url.split('/index')[0].split('/')[-1]
            download_dir_with_name = os.path.join(self.download_dir, name)
            if not os.path.exists(download_dir_with_name):
                os.makedirs(download_dir_with_name)
            print(download_dir_with_name)
            # 第一次请求的结果
            first_result_lines = requests.get(m3u8url).text
            # print(first_result_lines)
            # 拼接第二次请求链接
            new_m3u8url = ''
            # pH3tt6250076.ts like
            infoline = ''
            without_key = False
            without_key_head = ''
            for line in first_result_lines.split('\n'):
                if ('#' not in line):
                    if ('.m3u8' not in line) & (len(line.split('/')) > 2):
                        head = m3u8url.split('.com')[0] + '.com'
                        without_key_head = m3u8url.split('.com')[0] + '.com'
                        without_key = True
                    infoline = line
                    new_m3u8url = head + line  # https://cdn6-video.wwjingtou.com:8081/20191116/LNe9luPa/600kb/hls/index.m3u8
                    print(new_m3u8url)
            if not without_key:
                print(new_m3u8url)
                new_m3u8url_head = new_m3u8url.rsplit('/', 1)[0]  #
                print('new_m3u8url_head:', new_m3u8url_head)
                second_resulst_lines = requests.get(new_m3u8url).text
                print(second_resulst_lines)
                key = ""
                for line in second_resulst_lines.split('\n'):
                    if 'EXT-X-KEY' in line:
                        key_v = line.split(':')[1].split(',')
                        m = None
                        u = ''
                        for k_v in key_v:
                            if 'METHOD' in k_v:
                                m = k_v.replace('METHOD=', '')
                            if "URI" in k_v:
                                u = k_v.replace('URI=', '').replace('"', '')
                        key_url = new_m3u8url_head + '/' + u
                        print("key_url:", key_url)
                        key = requests.get(key_url).content
                    # print(key)
                    ts_name = ''
                    ts_url = ''
                    if '#EXT' not in line:
                        ts_url = (head + infoline + line).replace(tail, '')
                        ts_name = ts_url.split('/')[-1]

                        if not os.path.exists(os.path.join(self.download_dir, name)):
                            os.makedirs(os.path.join(self.download_dir, name))
                        ts_name = os.path.join(self.download_dir, name, line)
                        print(ts_name, ts_url)
                        ds = d_from_url(ts_name, ts_url, key)
                        ds.start()
                        # ds.join()
                    if 'EXT-X-ENDLIST' in line:
                        print('下载完毕')
            # 没有密钥
            else:
                for line in first_result_lines.split('\n'):
                    if '#EXT' not in line:
                        ts_url = without_key_head + line
                        ts_name = ts_url.split('/')[-1]

                        if not os.path.exists(os.path.join(self.download_dir, name)):
                            os.makedirs(os.path.join(self.download_dir, name))
                        ts_name = os.path.join(self.download_dir, name, ts_name)
                        print(ts_name, ts_url)
                        ds = d_from_url(ts_name, ts_url, key="")
                        ds.start()

        try:
            # merge_file(download_dir_with_name)
            pass
        except Exception as e:
            print('downloadm3u8', e)


def merge_file(path):
    time.sleep(10)
    os.chdir(path)
    cmd = "copy /b * new.tmp"
    os.system(cmd)
    os.system('del /Q *.ts')
    os.system('del /Q *.mp4')
    os.rename("new.tmp", "new.mp4")


# downloadm3u8(m3u8url='https://cdn6-video.wwjingtou.com:8081/20191113/CTpJmtzn/index.m3u8')
# downloadm3u8(m3u8url='https://sina.com-h-sina.com/20180820/11553_20d54bac/index.m3u8')
# downloadm3u8(m3u8url='https://youku.cdn7-okzy.com/20200116/16690_fad2bb53/index.m3u8')
# downloadm3u8(m3u8url='https://us2.wl-cdn.com/hls/20200114/8ca7354b88122021b68774b423897b15/1579008942/index.m3u8')
#downloadm3u8(m3u8url='https://youku.cdn7-okzy.com/20200113/16646_d6a84d8c/index.m3u8')
# downloadm3u8(m3u8url='https://fjgsix.slpchelp.com:8081/20200110/cDO5HTRo/index.m3u8')
# downloadm3u8(m3u8url='https://videox5-iqy.aclasselectricblanket.com:8081/20200103/P0qc3go3/index.m3u8')
# downloadm3u8(m3u8url='https://videox5-iqy.aclasselectricblanket.com:8081/20200103/cLwOSqHH/index.m3u8')
# downloadm3u8(m3u8url='https://videox5-iqy.aclasselectricblanket.com:8081/20200106/lC74zXv5/index.m3u')
# downloadm3u8(m3u8url='https://cdn5-video.shanxigemei.com:8081/20190612/GJnIyslv/index.m3u8')
# downloadm3u8(m3u8url='https://videox5-iqy.aclasselectricblanket.com:8081/20200107/nuwkaAkz/index.m3u8')
