# Georgosoulis Evangelos
# 12/2023
import pygame
import sys
import random
from time import sleep


# kinhsh pyrosvestwn
def movement(left, center, right, firef_x):

    button_pressed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # xeirismos me 1, 2, 3
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                firef_x = left
            elif event.key == pygame.K_3:
                firef_x = right
            elif event.key == pygame.K_2:
                firef_x = center
            # xeirismos me </> or A/D
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if firef_x == center:
                    firef_x = left
                elif firef_x == right:
                    firef_x = center
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if firef_x == center:
                    firef_x = right
                elif firef_x == left:
                    firef_x = center
        # GAMEPAD CONTROLS
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 1:  # O gia exit
                pygame.quit()
                sys.exit()
            # L1 kai <
            elif event.button == 9 or event.button == 13 and not button_pressed:
                button_pressed = True
                if firef_x == center:
                    firef_x = left
                elif firef_x == right:
                    firef_x = center
            # R1 kai >
            elif event.button == 10 or event.button == 14 and not button_pressed:
                button_pressed = True
                if firef_x == center:
                    firef_x = right
                elif firef_x == left:
                    firef_x = center
        elif event.type == pygame.JOYBUTTONUP:
            if (
                event.button == 9
                or event.button == 10
                or event.button == 13
                or event.button == 14
            ):
                button_pressed = False
    return firef_x


# arxiko menu
def main_menu(screen, black, width, height, sky_blue, controller):
    music = pygame.mixer.Sound("assets/8bit-music-for-game-68698.mp3")
    music.play()  # mousikh gia to menu mono
    music.set_volume(0.3)
    font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 20)
    titleFont = pygame.font.Font("assets/PressStart2P-Regular.ttf", 40)

    title = titleFont.render("Bouncing Babies", True, black)

    if controller:  # an anagnwristei controller
        # emfanise ta katallhla controls
        textStart = font.render("Press X to start the game", True, black)
        textInstr = font.render("< > or (L1, R1) to move", True, black)
        textExit = font.render("Press O to quit", True, black)
    else:
        textStart = font.render("Press SPACE to start the game", True, black)
        textInstr = font.render("< > or (1, 2, 3) to move", True, black)
        textExit = font.render("Press ESC to quit", True, black)

    title_rect = title.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 150)
    )  # kentrarismena
    textInstr_rect = textInstr.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2)
    )
    textStart_rect = textStart.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 25)
    )
    textExit_rect = textExit.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 50)
    )

    firef_size = 50
    center = width // 2 - firef_size // 2  # 3 pithana positions
    left = 100
    right = width - 100 - firef_size
    firef_x = center
    firef_y = height - 50
    firefighters_image = pygame.image.load("assets/firefighters2.png")
    firefighters_image = pygame.transform.scale(
        firefighters_image, (firef_size + 50, firef_size)
    )

    game_started = False
    screenshot = pygame.image.load("assets/screenshot.png")

    # dexetai pollapla inputs se kathe press sto controller xwris flag
    button_pressed = False

    # ta controls doulevoun kai sto start screen
    while not game_started:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_started = True
                    music.stop()
                    return game_started, firef_x
                elif event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_1:
                    firef_x = left
                elif event.key == pygame.K_3:
                    firef_x = right
                elif event.key == pygame.K_2:
                    firef_x = center
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if firef_x == center:
                        firef_x = left
                    if firef_x == right:
                        firef_x = center
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if firef_x == center:
                        firef_x = right
                    if firef_x == left:
                        firef_x = center
            # gamepad inputs - dokimasmeno gia ps4 controller
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # X button in controller
                    game_started = True
                    music.stop()
                    return game_started, firef_x
                elif event.button == 1:  # O button in controller
                    return False
                elif event.button == 9 or event.button == 13 and not button_pressed:
                    button_pressed = True
                    if firef_x == center:
                        firef_x = left
                    if firef_x == right:
                        firef_x = center
                elif event.button == 10 or event.button == 14 and not button_pressed:
                    if firef_x == center:
                        firef_x = right
                    if firef_x == left:
                        firef_x = center
            elif event.type == pygame.JOYBUTTONUP:
                if (
                    event.button == 9
                    or event.button == 10
                    or event.button == 13
                    or event.button == 14
                ):
                    button_pressed = False

        screen.blit(screenshot, (0, 0))
        firefighters = pygame.draw.rect(
            screen, sky_blue, (firef_x, firef_y, firef_size, firef_size)
        )
        screen.blit(firefighters_image, firefighters.topleft)
        screen.blit(title, title_rect)
        screen.blit(textInstr, textInstr_rect)
        screen.blit(textStart, textStart_rect)
        screen.blit(textExit, textExit_rect)
        pygame.display.update()

    return game_started, firef_x


# lives/wave/score menu
def draw_menu(width, screen, lives, waves, score, black, white):
    font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 20)
    pygame.draw.rect(
        screen, black, (0, 0, width, 50)
    )  # x=0, y=0, sizex = 900(width), sizey = 50

    menu_text = f"Lives: {lives}    Wave {waves}    Score: {score}"
    text_surface = font.render(menu_text, True, white)

    text_rect = text_surface.get_rect(center=(width // 2, 30))  # monima kentrarismena

    screen.blit(text_surface, text_rect)


# game over gia lives = 0
def game_over(screen, white, black, score, old_score, controller, joystick):
    if controller:
        joystick.rumble(1, 1, 1000)  # donhsh controller
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 20)
    titleFont = pygame.font.Font("assets/PressStart2P-Regular.ttf", 40)

    title = titleFont.render("Game Over", True, red)

    if old_score < score:  # an to neo score einai > tou highscore
        text = f"New High Score : {score}"
        old_score = score  # to neo highscore einai to score
    else:  # alliws emfanise to highscore
        text = f"High Score : {old_score}"

    if controller:
        textStart = font.render("Press X to start again the game", True, white)
        textExit = font.render("Press O to quit", True, white)
    else:
        textStart = font.render("Press SPACE to start again the game", True, white)
        textExit = font.render("Press ESC to quit", True, white)

    textHighScore = font.render(text, True, yellow)
    title_rect = title.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 150)
    )  # sto kentro
    textHighScore_rect = textHighScore.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 250)
    )
    textStart_rect = textStart.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 25)
    )
    textExit_rect = textExit.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 50)
    )

    game_started = False

    while not game_started:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # space = play again
                    game_started = True
                    return (
                        game_started,
                        old_score,
                    )  # epestrepse kai ananewmeno highscore
                elif event.key == pygame.K_ESCAPE:  # esc = exit
                    return False, old_score
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # X button in controller
                    game_started = True
                    return (
                        game_started,
                        old_score,
                    )
                elif event.button == 1:  # O button in controller
                    return False, old_score

        screen.fill(black)
        screen.blit(title, title_rect)
        screen.blit(textHighScore, textHighScore_rect)
        screen.blit(textStart, textStart_rect)
        screen.blit(textExit, textExit_rect)
        pygame.display.flip()


# allazei texture to mwro kathe fora
def baby_chooser(baby_size):
    # otan allazei to score h xanetai mia zwh
    rand = random.randint(0, 3)
    if rand == 0:
        baby_image = pygame.image.load("assets/hulk.png")
        baby_image = pygame.transform.scale(baby_image, (baby_size, baby_size))
    elif rand == 1:
        baby_image = pygame.image.load("assets/baby3.png")
        baby_image = pygame.transform.scale(baby_image, (baby_size, baby_size))
    elif rand == 2:
        baby_image = pygame.image.load("assets/baby.png")
        baby_image = pygame.transform.scale(baby_image, (baby_size, baby_size))
    elif rand == 3:
        baby_image = pygame.image.load("assets/baby2.png")
        baby_image = pygame.transform.scale(baby_image, (baby_size, baby_size))

    return baby_image


# ananewsh wave & speed paixnidiou
def wave_counter(score, waves, current_wave, clock_ticks):
    waveup = pygame.mixer.Sound("assets/message-incoming-132126.mp3")
    flag = False
    if score < 10:  # paramenei wave 1
        pass  # ginetai wave 0 kai de theloume auto
    else:  # kathe 10score +1wave
        waves = score // 10
        waves += 1
        flag = True

    if flag == True:
        if waves != current_wave:  # an auksithei to wave
            waveup.play()
            waveup.set_volume(0.2)
            current_wave = waves  # ananewse to gia epomenh fora
            clock_ticks += 5  # megalutero wave = megalutero speed
    return waves, current_wave, clock_ticks


# kinhsh mwrwn
def baby_movement(baby_y, baby_x, baby_velocity_x, baby_velocity_y):
    gravity = 0.5
    baby_y += baby_velocity_y
    baby_x += baby_velocity_x
    baby_velocity_y += gravity
    return baby_y, baby_x, baby_velocity_y


# reward +1 life
def extra_life(score_up, lives):
    # mono gia current lives < 5
    lifeup = pygame.mixer.Sound("assets/90s-game-ui-6-185099.mp3")
    if score_up == 25:  # kathe 25 pontous kerdizei mia zwh (max = 5)
        if lives < 5:
            lives += 1
            lifeup.play()
            lifeup.set_volume(0.1)
        score_up = 0
    return score_up, lives


def main():
    pygame.init()
    pygame.joystick.init()

    controller = False  # an anagnwristei controller h oxi
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"{joystick.get_name()} detected")
        controller = True
    else:
        joystick = False

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bouncing Babies")
    gameIcon = pygame.image.load("assets/baby.png")
    pygame.display.set_icon(gameIcon)
    clock = pygame.time.Clock()

    # xrwmata
    white = (255, 255, 255)
    black = (0, 0, 0)
    sky_blue = (0, 183, 239)

    # arxikopoihsh gia sizes kai positions
    firef_size = 50
    center = width // 2 - firef_size // 2  # 3 pithanes topothesies
    left = 100
    right = width - 100 - firef_size
    firef_x = center
    firef_y = height - 50

    baby_x = 100  # gia mwro
    baby_y = 100
    baby_size = 40
    baby_velocity_y = 0
    baby_velocity_x = 0
    rotation_angle = 0

    # sounds
    miss = pygame.mixer.Sound("assets/rblxSFX.mp3")
    boing = pygame.mixer.Sound("assets/boing_lmke36X.mp3")
    boing.set_volume(0.1)
    gameover_sound = pygame.mixer.Sound("assets/negative_beeps-6008.mp3")

    old_score = -1  # gia highscore se play again
    start_game, firef_x = main_menu(screen, black, width, height, sky_blue, controller)
    if not start_game:
        pygame.quit()
        sys.exit()

    # assets
    baby_image = pygame.image.load("assets/baby.png")
    baby_image = pygame.transform.scale(baby_image, (baby_size, baby_size))
    ambulance_image = pygame.image.load("assets/ambulance_cropped.png")
    ambulance_image = pygame.transform.scale(ambulance_image, (100, 100))
    firefighters_image = pygame.image.load("assets/firefighters2.png")
    firefighters_image = pygame.transform.scale(
        firefighters_image, (firef_size + 50, firef_size)
    )
    background = pygame.image.load("assets/background.png")
    background = pygame.transform.scale(background, (width, height))
    house_image = pygame.image.load("assets/apartment.png")
    house_image = pygame.transform.scale(house_image, (100, 500))

    # arxikes times tou upper menu
    waves = 1
    score = 0
    lives = 5  # max 5 zwes
    clock_ticks = 50  # game speed 50

    score_up = 0  # fores pou auksithike to score(gia +1 life)
    current_wave = 1

    while True:
        # kinhsh pyrosvestwn
        firef_x = movement(left, center, right, firef_x)
        # wave counter
        waves, current_wave, clock_ticks = wave_counter(
            score, waves, current_wave, clock_ticks
        )
        # kinhsh mwrwn
        baby_y, baby_x, baby_velocity_y = baby_movement(
            baby_y, baby_x, baby_velocity_x, baby_velocity_y
        )

        # epafh mwrou & pyrosvestwn
        if firef_x <= baby_x <= firef_x + firef_size and baby_y + baby_size >= firef_y:
            boing.play()
            baby_velocity_y = -12  # steilto panw
            baby_velocity_x = 6  # kai deksia

        if baby_y + baby_size > height:  # mwro katw
            miss.play()
            miss.set_volume(0.5)
            if controller:
                joystick.rumble(0, 1, 500)  # donhsh
            sleep(1.5)
            baby_image = baby_chooser(baby_size)
            lives -= 1
            if lives == 0:
                gameover_sound.play()
                gameover_sound.set_volume(0.4)
                start_again, old_score = game_over(
                    screen, white, black, score, old_score, controller, joystick
                )

                if not start_again:  # exit game
                    pygame.quit()
                    sys.exit()
                else:  # play again
                    waves = 1  # reset stis arxikes times
                    score = 0
                    lives = 5
                    clock_ticks = 50  # arxiko speed
                    firef_x = center
            baby_y = 100
            baby_x = 100
            baby_velocity_y = 0
            baby_velocity_x = 0
        if baby_x + baby_size > width:  # mwro eftase ambulance
            score += 1
            baby_image = baby_chooser(baby_size)
            baby_y = 100  # ksana sthn arxh
            baby_x = 100
            baby_velocity_y = 0
            baby_velocity_x = 0
            score_up += 1
            score_up, lives = extra_life(score_up, lives)

        # rotate to mwro sunexeia
        rotated_baby_image = pygame.transform.rotate(baby_image, rotation_angle)
        rotation_angle += -3

        screen.blit(background, (0, 0))
        house = pygame.draw.rect(screen, sky_blue, (0, 100, 100, 500))
        baby = pygame.draw.rect(
            screen,
            sky_blue,
            (baby_x, baby_y, baby_size, baby_size),
        )
        firefighters = pygame.draw.rect(
            screen, sky_blue, (firef_x, firef_y, firef_size, firef_size)
        )
        ambulance = pygame.draw.rect(
            screen, sky_blue, (width - 49, height - 100, 100, 100)
        )

        draw_menu(width, screen, lives, waves, score, black, white)

        screen.blit(rotated_baby_image, baby.topleft)
        screen.blit(ambulance_image, ambulance.topleft)
        screen.blit(firefighters_image, firefighters.topleft)
        screen.blit(house_image, house.topleft)

        pygame.display.flip()
        clock.tick(clock_ticks)


if __name__ == "__main__":
    main()
