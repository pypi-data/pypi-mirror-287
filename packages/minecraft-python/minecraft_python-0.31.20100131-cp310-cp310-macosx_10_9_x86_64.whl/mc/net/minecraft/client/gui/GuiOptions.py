from mc.net.minecraft.client.gui.GuiScreen import GuiScreen
from mc.net.minecraft.client.gui.GuiButton import GuiButton
from mc.net.minecraft.client.gui.GuiSmallButton import GuiSmallButton
from mc.net.minecraft.client.gui.GuiControls import GuiControls

class GuiOptions(GuiScreen):
    __screenTitle = 'Options'

    def __init__(self, screen, options):
        self.__parentScreen = screen
        self.__options = options

    def initGui(self):
        for i in range(self.__options.numberOfOptions):
            self._controlList.append(GuiSmallButton(i, self.width // 2 - 155 + i % 2 * 160,
                                                    self.height // 6 + 24 * (i >> 1),
                                                    self.__options.getOptionDisplayString(i)))

        self._controlList.append(GuiButton(100, self.width // 2 - 100,
                                           self.height // 6 + 120 + 12, 'Controls...'))
        self._controlList.append(GuiButton(200, self.width // 2 - 100,
                                           self.height // 6 + 168, 'Done'))

    def _actionPerformed(self, button):
        if button.enabled:
            if button.id < 100:
                self.__options.setOptionValue(button.id, 1)
                button.displayString = self.__options.getOptionDisplayString(button.id)
            elif button.id == 100:
                self.mc.displayGuiScreen(GuiControls(self, self.__options))
            elif button.id == 200:
                self.mc.displayGuiScreen(self.__parentScreen)

    def drawScreen(self, xm, ym):
        self._drawGradientRect(0, 0, self.width, self.height, 1610941696, -1607454624)
        self.drawCenteredString(self._fontRenderer, self.__screenTitle,
                                self.width / 2, 20, 16777215)
        super().drawScreen(xm, ym)
