# まずはpyxelをインポート
import pyxel

# ゲーム全体を表すクラスを作り、その中でゲームの内容を定義する
class App:
    def __init__(self):
        # 画面サイズ(幅w, 高さh)を指定する
        pyxel.init(100, 100)

        # とりあえず変数を作っておく
        # 今は特に意味はない
        self.x = 0

        # フレーム更新時に実行する更新関数と描画関数を登録する
        # 2つの関数が時間ごとに連続で実行されるイメージ
        pyxel.run(self.update, self.draw)

    def update(self):
        # # 1フレームごとにxが1増えていく
        # # 今は特に意味はない
        # self.x += 1
        
        # 右キーを押している間はxが増える
        if(pyxel.btn(pyxel.KEY_RIGHT)):
            self.x += 1
        # 押していなければ1になる
        elif(pyxel.btn(pyxel.KEY_LEFT)):
            self.x -= 1

            

    def draw(self):
        # 画面をクリアする色を指定する(0〜15)
        # 1フレームごとに画面が色0(=黒)でクリアされる
        # 今は特に意味はない
        pyxel.cls(0)
        
        # # 四角形を描画、引数は(左上の点の座標x, y, 幅w, 高さh, 色)
        # pyxel.rect(10, 10, 10, 10, 9)
        
        # 四角形を描画、引数は(左上の点の座標x, y, 幅w, 高さh, 色)
        # 変数xを幅に設定
        pyxel.rect(10, 10, self.x, 10, 9)
        
        # マウスカーソルの座標を取得
        mx = pyxel.mouse_x
        my = pyxel.mouse_y

        # 新しく四角形を作成
        # 左上の座標をマウスカーソルの座標と一致させる
        pyxel.rect(mx, my, 5, 5, 6)

# クラスのインスタンスを生成、ゲームを開始
App()