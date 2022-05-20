class Demon:

    def init(health, speed, damage):
        demon = Entity(model = 'sphere', color = color.red)
    def notice():
        if(distance(this, player) <= 15):
            aggro()

    def aggro():
        if(player.x > demon.x and distance(this, player) > .5):
            demon.x += .5
        if(player.x < demon.x and distance(this, player) > .5):
            demon.x -= .5
        if(player.z > demon.z and distance(this, player) > .5):
            demon.z += .5
        if(player.z < demon.z and distance(this, player) > .5):
            demon.z -= .5

    def attack():
        if(distance(this, player) <= 1):
            sleep(.1)
            player.setHealth(player.getHealth() - damage)
            
    def update():
        notice()
        attack()
