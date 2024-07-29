from mc.net.minecraft.game.level.block.Blocks import blocks
from mc.net.minecraft.game.item.Item import Item

class ItemFlintAndSteel(Item):

    def __init__(self, items, itemId):
        super().__init__(items, 3)
        self._maxStackSize = 1
        self._maxDamage = 64

    def onItemUse(self, stack, world, x, y, z, sideHit):
        if sideHit == 0: y -= 1
        if sideHit == 1: y += 1
        if sideHit == 2: z -= 1
        if sideHit == 3: z += 1
        if sideHit == 4: x -= 1
        if sideHit == 5: x += 1

        if x <= 0 or y <= 0 or z <= 0 or x >= world.width - 1 or y >= world.height - 1 or z >= world.length - 1:
            return

        blockId = world.getBlockId(x, y, z)
        if blockId == 0:
            world.setBlockWithNotify(x, y, z, blocks.fire.blockID)

        stack.damageItem(1)
