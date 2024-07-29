# cython: language_level=3

from libc.math cimport sqrt

from mc.JavaUtils cimport random
from mc.net.minecraft.client.render.Tessellator cimport Tessellator
from mc.net.minecraft.game.entity.Entity cimport Entity

cdef class EntityFX(Entity):

    def __cinit__(self):
        self._particleTextureIndex = 0
        self._particleGravity = 0.0

    def __init__(self, world, x, y, z, xr, yr, zr):
        Entity.__init__(self, world)
        self.setSize(0.2, 0.2)
        self.yOffset = self.height / 2.0
        self.setPosition(x, y, z)

        self._particleRed = self._particleGreen = self._particleBlue = 1.0
        self._motionX1 = xr + (random() * 2.0 - 1.0) * 0.4
        self._motionY1 = yr + (random() * 2.0 - 1.0) * 0.4
        self._motionZ1 = zr + (random() * 2.0 - 1.0) * 0.4
        speed = (random() + random() + 1.0) * 0.15

        dd = sqrt(self._motionX1 * self._motionX1 + self._motionY1 * self._motionY1 + self._motionZ1 * self._motionZ1)
        self._motionX1 = self._motionX1 / dd * speed * 0.4
        self._motionY1 = self._motionY1 / dd * speed * 0.4 + 0.1
        self._motionZ1 = self._motionZ1 / dd * speed * 0.4

        self._particleTextureJitterX = self._rand.nextFloat() * 3.0
        self._particleTextureJitterY = self._rand.nextFloat() * 3.0

        self._particleScale = (self._rand.nextFloat() * 0.5 + 0.5) * 2.0

        self._particleMaxAge = <int>(4 // (self._rand.nextFloat() * 0.9 + 0.1))
        self._particleAge = 0
        self._canTriggerWalking = False

    def multiplyVelocity(self, power):
        self._motionX1 *= 0.2
        self._motionY1 = (self._motionY1 - 0.1) * 0.2 + 0.1
        self._motionZ1 *= 0.2
        return self

    def multipleParticleScaleBy(self, scale):
        self.setSize(0.120000005, 0.120000005)
        self._particleScale *= 0.6
        return self

    def onEntityUpdate(self):
        self.prevPosX = self.posX
        self.prevPosY = self.posY
        self.prevPosZ = self.posZ

        if self._particleAge >= self._particleMaxAge:
            self.setEntityDead()

        self._particleAge += 1

        self._motionY1 = self._motionY1 - 0.04 * self._particleGravity
        self.moveEntity(self._motionX1, self._motionY1, self._motionZ1)
        self._motionX1 *= 0.98
        self._motionY1 *= 0.98
        self._motionZ1 *= 0.98

        if self.onGround:
            self._motionX1 *= 0.7
            self._motionZ1 *= 0.7

    def renderParticle(self, Tessellator t, float a, float xa, float ya,
                       float za, float xa2, float ya2):
        cdef float u0, u1, v0, v1, r, x, y, z, br

        u0 = (self._particleTextureIndex % 16) / 16.0
        u1 = u0 + 0.999 / 16.0
        v0 = (self._particleTextureIndex // 16) / 16.0
        v1 = v0 + 0.999 / 16.0
        r = 0.1 * self._particleScale

        x = self.prevPosX + (self.posX - self.prevPosX) * a
        y = self.prevPosY + (self.posY - self.prevPosY) * a
        z = self.prevPosZ + (self.posZ - self.prevPosZ) * a

        br = self.getBrightness(a)
        t.setColorOpaque_F(self._particleRed * br, self._particleGreen * br,
                           self._particleBlue * br)
        t.addVertexWithUV(x - xa * r - xa2 * r, y - ya * r,
                          z - za * r - ya2 * r, u0, v1)
        t.addVertexWithUV(x - xa * r + xa2 * r, y + ya * r,
                          z - za * r + ya2 * r, u0, v0)
        t.addVertexWithUV(x + xa * r + xa2 * r, y + ya * r,
                          z + za * r + ya2 * r, u1, v0)
        t.addVertexWithUV(x + xa * r - xa2 * r, y - ya * r,
                          z + za * r - ya2 * r, u1, v1)

    def getFXLayer(self):
        return 0

    def _writeEntityToNBT(self, compound):
        pass

    def _getEntityString(self):
        return None

    def _readEntityFromNBT(self):
        pass
