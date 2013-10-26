# "Personality Rights" Copyright 2013 Sumana Harihareswara.
# Distributed under the GNU Public License, version 3.
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

image accordion = "Paris_-_Accordion_Player_-_0956.jpg"
# https://commons.wikimedia.org/wiki/File:Paris_-_Accordion_Player_-_0956.jpg
image turtle = "Green_Sea_Turtle_grazing_seagrass.jpg"
# https://commons.wikimedia.org/wiki/File:Green_Sea_Turtle_grazing_seagrass.jpg
image crystals = "Cristales_cueva_de_Naica.jpg"
# https://commons.wikimedia.org/wiki/File:Cristales_cueva_de_Naica.JPG
image orchids = "Orchis_tridentata-Blueten-2.jpg"
# https://commons.wikimedia.org/wiki/File:Orchis_tridentata-Blueten-2.jpg
image zebra = "Equus_quagga_Namutoni_2012.jpg"
# https://commons.wikimedia.org/wiki/File:Equus_quagga_%28Namutoni,_2012%29.jpg
image rowboat = "Rowing_boat_on_a_house_roof_-_Fira_-_Santorini_-_Greece_-_02.jpg"
# https://commons.wikimedia.org/wiki/File:Rowing_boat_on_a_house_roof_-_Fira_-_Santorini_-_Greece_-_02.jpg
image castle = "Vyborg_06-2012_Castle_06.jpg"
# https://commons.wikimedia.org/wiki/File:Vyborg_06-2012_Castle_06.jpg

# Declare characters used by this game.
define m = Character('Me', color="#c8c8ff", show_two_window=True)
define h = Character('HappySappy99', color="#cccccc", show_two_window=True)
define narrator = Character(None, window_left_padding=160)
define credits = Character(None, italics=True)

# The game starts here.
label start:
      scene black

      m "Hey, HappySappy. Want to work the Articles for Creation queue with me tonight?"

      "Silence."

      h "But you're a ghost!"

      play music "InterestingPlacesToDie.ogg"
# http://www.crummy.com/music/version_1.1.2pl14/

menu:
    "So what?":
        jump denial

    "I'm a ghost?!":
        jump ghost

    "I .... don't know what else to do.":
        jump wander

label denial:
      scene zebra
      with dissolve

      "I shut the window, minimized all my apps.{w} The desktop background was soothing."

      "{i}She doesn't know what she's talking about.{w} There's no reason dead people can't make valuable contributions in today's society.{w} She's always been a deletionist anyway.{/i}"
      jump HSconv

label ghost:
    m "I do not believe in ghosts.{w} I am a paid-up member of my local skeptics society.{p}Was.{w} (was?)"
    jump HSconv

label wander:
      m "It's just hard for me to believe that, you know. It's over."
      h "Could you accept your fate?"
      m "Not really."
      h "That does make things a little harder."

      scene orchids
      with dissolve

      "I felt the pull of far-off repositories of images, knowledge.{p}Photons that not enough retinas had seen."

      "In life I'd been a brain in a jar, really. So I wandered my old stomping grounds.{p}Wikipedia."

      "I'm a ghost. You'd think ghosts would feel no need to click around Wikipedia.{w} You'd think Wikipedia would only be for living people.{p}You'd think a lot of things."

      "Adminship requests, Did You Know, vandalism, barnstars.{w} The susurrations and rhythms of my former life began to feel pleasantly unfamiliar.{w} My absence made room for new young leaders to grow."

      "My own atoms and specks of light began to fade, and with them, my attachment to that engine of constant change.{p} I'd always known it would outlive me."
      
      scene castle
      with dissolve
      "Death is a room.{p}Dying is an action applying to nothing.{p}My body was now a haunted house."

      show rowboat
      with dissolve

      "I was coming to understand that my momentum wouldn't carry me any further."
      jump bigquestion

label HSconv:
    m "It is impossible for me to be a ghost."
    h "I know you are dead. I updated your userpage myself."
    h "Go away. You belong ... I don't know. Where dead people go."

    jump bigquestion

label bigquestion:
      show accordion

      "Is the fact that our consciousness ends an unbearably frightening specter?"

menu:
    "{i}terror{/i}":
        jump slippingthroughfingers

    "Reality is that which, when you stop believing in it, does not go away. And I, perversely, {b}am{/b} going away...":
        jump fulfillingclosure


label slippingthroughfingers:
      "I tried to concentrate hard on the screen in front of me."

      show crystals

      "A forest of scintillating spikes accelerated towards me.{p}No please{w} stop{w} it wasn't enough time"

      scene black
      jump endcredits

label fulfillingclosure:
      scene turtle
      with dissolve

      "I had finally withdrawn into the shell I had always wanted.{p}The last thing I saw was greenish light, warming me like a distant sun through gently swaying waters."

      jump endcredits

label endcredits:
      "credits" "Thank you for playing {b}Personality Rights{/b} by Sumana Harihareswara (licensed GPL). Thanks to Ren'Py, Wikimedia Commons, and Leonard Richardson for software, photos, and music.\nFor more info, please see {a=http://www.panix.com/~sumanah/personalityrights.html}the game's webpage{/a}."

      return