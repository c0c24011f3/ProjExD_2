import os
import random 
import sys
import pygame as pg
import time #課題１


WIDTH, HEIGHT = 1100, 650
DELTA = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
     
    """
    引数：こうかとんRectかばくだんRect
    戻り値：タプル（横方向判定結果、縦方向判定結果）
    画面内ならTrue,画面外ならFalse
     """

    yoko, tate = True, True
    if rct.left < 0 or WIDTH <rct.right:  
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:  
        tate = False
    return yoko, tate


def kadai1(screen: pg.Surface) -> None:
    """
    ゲームオーバー時に画面をブラックアウトし、
    「Game Over」と泣いているこうかとんを表示する関数
    """
    # 1. 黒い矩形を描画するための空のSurfaceを作り、黒で塗りつぶす
    black_scr = pg.Surface((WIDTH, HEIGHT))
    black_scr.fill((0, 0, 0))
    
    # 2. 1のSurfaceの透明度を設定する（半透明）
    black_scr.set_alpha(200)
    
    # 3. 白文字でGame Overと書かれたフォントSurfaceを作り、1のSurfaceにblitする
    fonto = pg.font.Font(None, 80)
    txt_img = fonto.render("Game Over", True, (255, 255, 255))
    txt_rct = txt_img.get_rect()
    txt_rct.center = WIDTH // 2, HEIGHT // 2
    black_scr.blit(txt_img, txt_rct)

    # 4. こうかとん画像をロードし、こうかとんSurfaceを作り、1のSurfaceにblitする
    # ※fig/6.pngに変更
    try:
        kk_img = pg.image.load("fig/6.png")
        kk_img = pg.transform.rotozoom(kk_img, 0, 0.9)
        
        # 文字の左右に配置（画像参照）
        kk_rct_left = kk_img.get_rect()
        kk_rct_left.midright = (txt_rct.left - 20, txt_rct.centery)
        black_scr.blit(kk_img, kk_rct_left)
        
        kk_rct_right = kk_img.get_rect()
        kk_rct_right.midleft = (txt_rct.right + 20, txt_rct.centery)
        black_scr.blit(kk_img, kk_rct_right)
    except FileNotFoundError:
        print("画像 fig/8.png が見つかりませんでした")

    # 5. 1のSurfaceをscreen Surfaceにblitする
    screen.blit(black_scr, (0, 0))

    # 6. pg.display.update()したら，5秒表示する
    pg.display.update()
    time.sleep(5)



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img, (255,0,0),(10,10),10)
    bb_img.set_colorkey((0,0,0))
    bb_rct = bb_img.get_rect()
    bb_rct.centerx = random.randint(0,WIDTH)
    bb_rct.centery = random.randint(0,HEIGHT)
    vx, vy =+5, +5
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            

        if kk_rct.colliderect(bb_rct):     #課題１
            kadai1(screen)
            return
       # if kk_rct.colliderect(bb_rct):  
        #    print("ゲームオーバー")
         #   return

        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
       # if key_lst[pg.K_UP]:
        #    sum_mv[1] -= 5
        #if key_lst[pg.K_DOWN]:
         #   sum_mv[1] += 5
        #if key_lst[pg.K_LEFT]:
         #   sum_mv[0] -= 5
        #if key_lst[pg.K_RIGHT]:
         #   sum_mv[0] += 5
        #kk_rct.move_ip(sum_mv)
      #  screen.blit(kk_img, kk_rct)
       # pg.display.update()
       # tmr += 1
      #  clock.tick(50)
        for key, mv in DELTA.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]  
                sum_mv[1] += mv[1]  
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):  
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])  
        screen.blit(kk_img, kk_rct)
        yoko, tate = check_bound(bb_rct)
        if not yoko:  
            vx *= -1
        if not tate:  
            vy *= -1
        bb_rct.move_ip(vx, vy)
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)



        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx, vy)
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
