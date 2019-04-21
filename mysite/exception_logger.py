import sys,os
import traceback
from datetime import * 
from time import mktime
from django.views.defaults import server_error as default_server_error

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def server_error(request, *args, **kw):
    """ djangoのディフォルトエラーハンドラー
	django.conf.urls.defaults.server_error
	の代わりに500エラーを処理する。DEBUG==Falseの場合のみ。
	詳細をログに書き、ブラウザへの返答はジャンゴに任せる。
	使い方： 以下のコードをurls.pyなどに入れる。
        handler500='ext.exception_logger.server_error' 

        DEBUG=Falseの時のデバッグ手段
        http://d.hatena.ne.jp/karasuyamatengu/20100521/1274399876

    """
    # 開発モードでブラウザに送られるリスポンスオブジェクトを作る。
    from django.views import debug
    exc_info = sys.exc_info()
    rsp=debug.technical_500_response(request, *exc_info)

    # ログファイル名： path-to-view.timestamp.html
    dumpfile='.'.join([request.path_info.lstrip('/').rstrip('/').replace('/','-'), str(int(mktime(datetime.now().timetuple()))), 'html'])
    dumppath=os.path.join(BASE_DIR, dumpfile)

    # リスポンスからHTMLを取り出してログファイルに出力。
    #open(dumppath,'w').write(rsp.content)
    open(dumppath,'w').write(str(rsp.content))

    # ブラウザへの返答はジャンゴに任せる。(500.htmlテンプレートでページを作って返す)
    return default_server_error(request, *args, **kw)

