import pygame
from pygame.locals import *
from .GameState import GameState
from .SelectState import SelectState

class AnimateState(GameState):
    def __init__(self, stateSwitcher): super().__init__(stateSwitcher)
    def Initialize(self):
        print('アニメーション開始。')
    def Finalize(self):
        print('アニメーション演出終了。たとえばアニメーションの最中なら強制的に完了した状態にする。')
    def Event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: self.Switcher.Next()
            elif event.key == K_s: self.Switcher.Select(SelectState)
    def Draw(self, screen): screen.fill((0,255,0))
