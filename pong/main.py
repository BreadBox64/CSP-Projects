# dynamic polygonal pong

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import pygame, math, keyboard, socket, packing, _thread, json

pygame.font.init()
screen = pygame.display.set_mode([1000, 500])
pygame.display.set_caption("multiplayer polygonal pong prototype... why am i doing this?")
_clock = pygame.time.Clock()

ball_position = [0, 0]
current_board_sides = 4

username = input("Username (max. 12 chars): ")[:12]
my_position = 0.5
my_score = 0

IP = "76.92.172.78"
PORT = 42069 # :O

client = socket.socket()
client.connect((IP, PORT))

current_players = {

}

FONT = pygame.font.SysFont(None, 16)

my_side = 0

class Net():
    def __send_packet(data):
        client.sendall(packing.VarInt.Write(len(data)) + data)
    def LoginPacket(username):
        Net.__send_packet(
            packing.VarInt.Write(0) + packing.String.Write(username)
        )
    def SendUpdatePacket(my_pos):
        # send my pos, get players and ball position and my score back
        Net.__send_packet(
            packing.VarInt.Write(1) + packing.Float.Write(my_pos)
        )

def get_packet(conn):
    packet_length = packing.VarInt.ReadFromStream(conn)
    if packet_length == 0: return (-1, b"")

    packet_data = b""
    while len(packet_data) < packet_length:
        packet_data += conn.recv(packet_length - len(packet_data))
    
    packet_data, packet_id = packing.VarInt.Read(packet_data)
    return packet_id, packet_data

has_gotten_data = False

def net_recv_thread():
    global ball_position, current_players, my_score, my_side, has_gotten_data

    while True:
        p_id, p_dat = get_packet(client)

        if p_id == 0:
            data = json.loads(packing.String.Read(p_dat)[1])

            ball_position = data["ball"]
            current_players = data["players"]
            my_score = data["score"]

            has_gotten_data = True
        elif p_id == 1:
            p_dat, my_side = packing.VarInt.Read(p_dat)

def lerp(a, b, t):
    return a + (b - a) * t

def lerp2d(x1, y1, x2, y2, percentage):
    return lerp(x1, x2, percentage), lerp(y1, y2, percentage)

class ScreenRelated():
    def DrawBall():
        pygame.draw.circle(screen, (255, 255, 255), (500 + ball_position[0], 250 + ball_position[1]), 4)
    
    def DrawMap():
        for side in range((len(current_players))):
            a = 2 * math.pi / (len(current_players)) * side
            b = 2 * math.pi / (len(current_players)) * (side + 1)

            c = (0, 255, 0)
            if side == my_side: c = (255, 255, 0)
            pygame.draw.line(screen, c, (
                math.sin(a) * 200 + 500, math.cos(a) * 200 + 250
            ), (
                math.sin(b) * 200 + 500, math.cos(b) * 200 + 250
            ))

    def DrawPlayerNameOnSide(side, name, score):
        if len(name) > 12:
            name = name[:10]
        
        a = 2 * math.pi / (len(current_players)) * side
        b = 2 * math.pi / (len(current_players)) * (side + 1)

        midp = lerp(a, b, 0.5)

        newp = lerp2d(*(math.sin(midp) * 200 + 500, math.cos(midp) * 200 + 250), *(500, 250), -0.2)

        name = FONT.render(name, True, (255, 0, 255))
        screen.blit(name, (newp[0] - name.get_width() / 2, newp[1] - name.get_height() / 2))

        score = FONT.render("Score: " + str(score), True, (255, 0, 255))
        screen.blit(score, (newp[0] - score.get_width() / 2, newp[1] - score.get_height() / 2 + 10))

    def DrawPaddleOnSide(side, position): # position is between 0 and 1
        if not (0 <= position <= 1): return

        a = 2 * math.pi / (len(current_players)) * side
        b = 2 * math.pi / (len(current_players)) * (side + 1)

        new_pos = position / 5 * 4

        f = lerp2d(
            math.sin(a) * 200 + 500, math.cos(a) * 200 + 250,
            math.sin(b) * 200 + 500, math.cos(b) * 200 + 250,
            new_pos + 0.1 + 0.1
        )

        f2 = lerp2d(
            math.sin(a) * 200 + 500, math.cos(a) * 200 + 250,
            math.sin(b) * 200 + 500, math.cos(b) * 200 + 250,
            new_pos + 0.1 - 0.1
        )

        pygame.draw.line(screen, (0, 255, 255), f, f2, 3)

        pygame.draw.circle(screen, (0, 255, 255), f, 1)
        pygame.draw.circle(screen, (0, 255, 255), f2, 1)

        if side == my_side:
            pygame.draw.circle(screen, (255, 255, 0), (math.sin(a) * 200 + 500, math.cos(a) * 200 + 250,), 3)
            pygame.draw.circle(screen, (255, 255, 0), (math.sin(b) * 200 + 500, math.cos(b) * 200 + 250,), 3)

_thread.start_new_thread(net_recv_thread, ())

Net.LoginPacket(username)

waiting_font = pygame.font.SysFont(None, 36)
while True:
    _clock.tick(20)
    Net.SendUpdatePacket(my_position)

    print(ball_position)

    if has_gotten_data:
        print(current_players)

        if len(current_players) < 3:
            waiting_text = waiting_font.render("Waiting for more players ({0} / 3)...".format(len(current_players)), True, (255, 255, 255))
            screen.blit(waiting_text, (10, 10))

            pygame.display.flip()

            screen.fill((0, 0, 0))

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    client.close()
                    pygame.quit()
                    quit()
        else:
            ScreenRelated.DrawBall()

            ScreenRelated.DrawMap()
            
            for side in range(len(current_players)):
                if str(side) in current_players:
                    if not side == my_side:
                        ScreenRelated.DrawPaddleOnSide(side, current_players[str(side)]["pos"])
                        ScreenRelated.DrawPlayerNameOnSide(side, current_players[str(side)]["name"], current_players[str(side)]["score"])
                    else:
                        ScreenRelated.DrawPaddleOnSide(side, my_position)
                        ScreenRelated.DrawPlayerNameOnSide(side, username, my_score)

            if keyboard.is_pressed("a"):
                my_position = max(0, my_position - 0.05)
            if keyboard.is_pressed("d"):
                my_position = min(1, my_position + 0.05)

            pygame.display.flip()
            screen.fill((0, 0, 0))

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    client.close()
                    pygame.quit()
                    quit()