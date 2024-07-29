from mc.net.minecraft.client.Session import Session
from mc.net.minecraft.client.controller.PlayerController import PlayerController
from mc.net.minecraft.game.level.MobSpawner import MobSpawner
from mc.net.minecraft.game.level.block.Blocks import blocks
from mc.net.minecraft.game.item.ItemStack import ItemStack

class PlayerControllerCreative(PlayerController):

    def onRespawn(self, player):
        for i in range(9):
            if player.inventory.mainInventory[i] is None:
                player.inventory.mainInventory[i] = ItemStack(blocks.blocksList[Session.registeredBlocksList[i].blockID])
            else:
                player.inventory.mainInventory[i].stackSize = 1

    def shouldDrawHUD(self):
        return False

    def onWorldChange(self, world):
        super().onWorldChange(world)
        world.survivalWorld = False

        self.__mobSpawner = MobSpawner(world)
        size = world.width * world.length * world.height // 64 // 64 // 64
        for i in range(size):
            self.__mobSpawner.spawnMob(size, world.playerEntity, None)

    def onUpdate(self):
        self.__mobSpawner.spawnMobs()
