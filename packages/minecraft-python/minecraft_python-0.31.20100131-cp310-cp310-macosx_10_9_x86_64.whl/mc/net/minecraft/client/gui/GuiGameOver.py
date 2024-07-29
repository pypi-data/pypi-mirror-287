from mc.net.minecraft.client.gui.GuiLoadLevel import GuiLoadLevel
from mc.net.minecraft.client.gui.GuiNewLevel import GuiNewLevel
from mc.net.minecraft.client.gui.GuiOptions import GuiOptions
from mc.net.minecraft.client.gui.GuiScreen import GuiScreen
from mc.net.minecraft.client.gui.GuiButton import GuiButton
from pyglet import gl

class GuiGameOver(GuiScreen):

    def initGui(self):
        self._controlList.clear()
        self._controlList.append(GuiButton(1, self.width // 2 - 100, self.height // 4 + 72,
                                           'Generate new world...'))
        self._controlList.append(GuiButton(2, self.width // 2 - 100, self.height // 4 + 96,
                                           'Load world..'))
        if not self.mc.session:
            self._controlList[2].enabled = False

    def _keyTyped(self, key, char, motion):
        pass

    def _actionPerformed(self, button):
        if button.id == 0:
            self.mc.displayGuiScreen(GuiOptions(self, self.mc.options))
        elif button.id == 1:
            self.mc.displayGuiScreen(GuiNewLevel(self))
        elif button.id == 2 and self.mc.session:
            self.mc.displayGuiScreen(GuiLoadLevel(self))

    def drawScreen(self, xm, ym):
        self._drawGradientRect(0, 0, self.width, self.height, 0x60500000, -1602211792)
        gl.glPushMatrix()
        gl.glScalef(2.0, 2.0, 2.0)
        self.drawCenteredString(self._fontRenderer, 'Game over!', self.width // 2 // 2, 30, 0xFFFFFF)
        gl.glPopMatrix()
        self.drawCenteredString(self._fontRenderer, 'Score: &e' + str(self.mc.thePlayer.getScore()),
                                self.width // 2, 100, 0xFFFFFF)
        super().drawScreen(xm, ym)
