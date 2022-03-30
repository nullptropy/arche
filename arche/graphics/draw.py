# coding: utf-8

import pygame

def clear(ctx, color):
    ctx.screen.fill(color)

def rect(ctx, *a, **k):
    pygame.draw.rect(ctx.screen, *a, **k)