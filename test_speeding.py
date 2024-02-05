import sys
import tkinter as tk
from speed_class import SelfSpeed
import speed_class
from unittest import mock
from Gui import TypeSpeedGUI


def test_greenorred():
    var2 =TypeSpeedGUI('emptyfile.txt',root=tk.Tk())
    var2.make_page_3()
    var2.speed_game.start_page()
    var2.speed_game.start_with_unlimited_pack()
    var2.speed_game.start_with_unlimited_time()
    var2.speed_game.labelLeft.config(text="hello")
    var2.speed_game.GreenorRedLabel.config(text="hello")
    var2.speed_game.greenorred()
    assert var2.speed_game.GreenorRedLabel.cget("foreground") == "green"
    var2.speed_game.labelLeft.config(text="goodbye")
    var2.speed_game.GreenorRedLabel.config(text="hello")
    var2.speed_game.greenorred()
    assert var2.speed_game.GreenorRedLabel.cget("foreground") == "red"

def test_write_to_json():
    var2 =TypeSpeedGUI('emptyfile.txt',root=tk.Tk())
    var2.make_page_3()
    var2.speed_game.start_page()
    var2.speed_game.start_with_unlimited_pack()
    var2.speed_game.start_with_unlimited_time()
    var2.speed_game.labelLeft.config(text= "ala ma kota")
    var2.speed_game.time = 59
    var2.speed_game.stopTest()
    if var2.speed_game.time == 0:
        pass
    else:
        var2.speed_game.write_to_json()
    assert var2.speed_game.data[len(var2.speed_game.data)-1]
    assert var2.speed_game.data[len(var2.speed_game.data)-1]['time'] ==  59
    assert var2.speed_game.data[len(var2.speed_game.data)-1]['characters'] ==  9
    assert var2.speed_game.data[len(var2.speed_game.data)-1]['words'] ==  3
    assert var2.speed_game.data[len(var2.speed_game.data)-1]['game_mode'] == "unlimited_time"

def test_keypress(monkeypatch):
    var2 =TypeSpeedGUI('emptyfile.txt',root=tk.Tk())
    var2.make_page_3()
    var2.speed_game.start_page()
    var2.speed_game.start_with_unlimited_pack()
    var2.speed_game.start_with_unlimited_time()
    var2.speed_game.labelRight.config(text="ala")
    event = mock.Mock()
    monkeypatch.setattr(event,'keycode', (30))
    monkeypatch.setattr(event,'char','a')
    var2.speed_game.keyPress(event)
    assert var2.speed_game.labelLeft.cget('text') == "a"
    assert var2.speed_game.labelRight.cget('text') == "la"
    assert var2.speed_game.currentLetterLabel.cget('text') == "l"

def test_keypress2(monkeypatch):
    var4 =TypeSpeedGUI('emptyfile.txt',root=tk.Tk())
    var4.make_page_3()
    var4.speed_game.start_page()
    var4.speed_game.start_with_unlimited_pack()
    var4.speed_game.start_with_unlimited_time()
    var4.speed_game.labelLeft.config(text="")
    var4.speed_game.labelRight.config(text="ala")
    event = mock.Mock()
    monkeypatch.setattr(event,'keycode', (21))
    monkeypatch.setattr(event,'char','t')
    var4.speed_game.keyPress(event)
    event2 = mock.MagicMock()
    monkeypatch.setattr(event2,'keycode', (22))
    monkeypatch.setattr(event2,'char','')
    var4.speed_game.keyPress(event2)
    assert var4.speed_game.labelLeft.cget('text') == ""
    assert var4.speed_game.labelRight.cget('text') == "ala"

def test_keypress3(monkeypatch):
    var5 =TypeSpeedGUI('emptyfile.txt',root=tk.Tk())
    var5.make_page_3()
    var5.speed_game.start_page()
    var5.speed_game.start_with_unlimited_pack()
    var5.speed_game.start_with_unlimited_time()
    event = mock.Mock()
    monkeypatch.setattr(event,'keycode', (30))
    monkeypatch.setattr(event,'char','a')
    var5.speed_game.keyPress(event)
    event3 = mock.MagicMock()
    monkeypatch.setattr(event3,'char',' ')
    monkeypatch.setattr(event3,'keycode', (65))
    try:
        var5.speed_game.keyPress(event3)
        assert var5.speed_game.labelLeft.cget('text') == 'a'
        assert var5.speed_game.labelRight.cget('text') == " miala kota "
    except tk.TclError:
        pass

def test_keypress4(monkeypatch):
    var3 =TypeSpeedGUI('emptyfile.txt',root=tk.Tk())
    var3.make_page_3()
    var3.speed_game.start_page()
    var3.speed_game.start_with_unlimited_pack()
    var3.speed_game.start_with_unlimited_time()
    var3.speed_game.labelLeft.config(text="")
    var3.speed_game.labelRight.config(text="ala laa")
    event = mock.Mock()
    monkeypatch.setattr(event,'keycode', (32))
    event.char = 's'
    var3.speed_game.keyPress(event)
    assert var3.speed_game.labelLeft.cget('text') == "s"
    assert var3.speed_game.labelRight.cget('text') == "ala laa"

def test_keypress5(monkeypatch):
    var3 =TypeSpeedGUI('emptyfile.txt',root=tk.Tk())
    var3.make_page_3()
    var3.speed_game.start_page()
    var3.speed_game.start_with_unlimited_pack()
    var3.speed_game.start_with_unlimited_time()
    var3.speed_game.labelLeft.config(text="")
    var3.speed_game.labelRight.config(text="ala laa")
    event = mock.Mock()
    monkeypatch.setattr(event,'keycode', (30))
    event.char = 'a'
    var3.speed_game.keyPress(event)
    event2 = mock.Mock()
    monkeypatch.setattr(event2,'keycode', (39))
    event2.char = 'l'
    var3.speed_game.keyPress(event2)
    event3 = mock.Mock()
    monkeypatch.setattr(event3,'keycode', (30))
    event3.char = 'a'
    var3.speed_game.keyPress(event3)
    event4 = mock.Mock()
    monkeypatch.setattr(event4,'keycode', (65))
    event4.char = ''
    var3.speed_game.keyPress(event4)
    assert var3.speed_game.labelLeft.cget('text') == "ala"
    assert var3.speed_game.labelRight.cget('text') == " laa"




