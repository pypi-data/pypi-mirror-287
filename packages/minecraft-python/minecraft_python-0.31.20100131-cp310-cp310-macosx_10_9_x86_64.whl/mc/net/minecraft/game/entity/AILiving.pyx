# cython: language_level=3

cimport cython

from libc.math cimport floor, atan2, sqrt, pi

from mc.net.minecraft.game.physics.Vec3D import Vec3D
from mc.net.minecraft.game.entity.Entity cimport Entity
from mc.net.minecraft.game.entity.EntityLiving cimport EntityLiving
from mc.net.minecraft.game.level.World cimport World
from mc.JavaUtils cimport Random

cdef class AILiving:

    def __cinit__(self):
        self.__rand = Random()
        self._moveStrafing = 0.0
        self._moveForward = 0.0
        self.__randomYawVelocity = 0.0
        self.__entityLiving = None
        self._isJumping = False
        self.__fire = 0
        self.__moveSpeed = 0.7
        self.__entityAge = 0
        self.__playerToAttack = None

    def onLivingUpdate(self, World world, EntityLiving mob):
        cdef Entity entity
        cdef bint isInWater, isInLava
        cdef float xd, yd, zd

        self.__entityAge += 1
        if self.__entityAge > 600 and self.__rand.nextInt(800) == 0:
            entity = world.getPlayerEntity()
            if entity:
                xd = entity.posX - mob.posX
                yd = entity.posY - mob.posY
                zd = entity.posZ - mob.posZ
                if xd * xd + yd * yd + zd * zd < 1024.0:
                    self.__entityAge = 0
                else:
                    mob.setEntityDead()

        self.__entityLiving = mob
        if self.__fire > 0:
            self.__fire -= 1

        if mob.health <= 0:
            self._isJumping = False
            self._moveStrafing = 0.0
            self._moveForward = 0.0
            self.__randomYawVelocity = 0.0
        else:
            self.updatePlayerActionState()

        isInWater = mob.handleWaterMovement()
        isInLava = mob.handleLavaMovement()
        if self._isJumping:
            if isInWater:
                mob.motionY += 0.04
            elif isInLava:
                mob.motionY += 0.04
            elif mob.onGround:
                self.__entityLiving.motionY = 0.42

        self._moveStrafing *= 0.98
        self._moveForward *= 0.98
        self.__randomYawVelocity *= 0.9
        mob.travel(self._moveStrafing, self._moveForward)
        entities = world.getEntitiesWithinAABBExcludingEntity(mob, mob.boundingBox.expand(0.2, 0.0, 0.2))
        if entities and len(entities) > 0:
            for entity in entities:
                if not entity.canBePushed():
                    continue

                entity.applyEntityCollision(mob)

    def updatePlayerActionState(self):
        if self.__rand.nextFloat() < 0.07:
            self._moveStrafing = (self.__rand.nextFloat() - 0.5) * self.__moveSpeed
            self._moveForward = self.__rand.nextFloat() * self.__moveSpeed

        self._isJumping = self.__rand.nextFloat() < 0.01
        if self.__rand.nextFloat() < 0.04:
            self.__randomYawVelocity = (self.__rand.nextFloat() - 0.5) * 60.0

        self.__entityLiving.rotationYaw += self.__randomYawVelocity
        self.__entityLiving.rotationPitch = 0.0

        if self.__entityLiving.handleWaterMovement() or self.__entityLiving.handleLavaMovement():
            self._isJumping = self.__rand.nextFloat() < 0.8
