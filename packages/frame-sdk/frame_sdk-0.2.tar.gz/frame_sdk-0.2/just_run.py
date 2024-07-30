import asyncio
import datetime
import os
import random
from src.frame_sdk import Bluetooth, Frame
from src.frame_sdk.display import Alignment


async def main():
    async with Frame() as f:
        print(f"Connected: {f.bluetooth.is_connected()}")
        # let's get the current battery level
        print(f"Frame battery: {await f.get_battery_level()}%")
        await f.bluetooth.send_break_signal()
        await f.files.delete_file("/lib/prntLng.lua")
        await f.bluetooth.send_reset_signal()

    async with Frame() as f:
        f.bluetooth.print_debugging = True
        # you can access the lower-level bluetooth connection via f.bluetooth, although you shouldn't need to do this often
        print(f"Connected: {f.bluetooth.is_connected()}")

        # let's get the current battery level
        print(f"Frame battery: {await f.get_battery_level()}%")
        
        # set a homescreen via script and callback
        await f.run_on_wake("""frame.display.text('Battery: ' .. frame.battery_level() ..  '%', 10, 10);
                            if frame.time.utc() > 10000 then
                                local time_now = frame.time.date();
                                frame.display.text(time_now['hour'] .. ':' .. time_now['minute'], 300, 160);
                                frame.display.text(time_now['month'] .. '/' .. time_now['day'] .. '/' .. time_now['year'], 300, 220) 
                            end;
                            frame.display.show();
                            frame.sleep(10);
                            frame.display.text(' ',1,1);
                            frame.display.show();
                            frame.sleep()""")
        
        print("Tap the Frame to continue...")
        await f.display.show_text("Tap the Frame to continue...", align=Alignment.MIDDLE_CENTER)
        await f.motion.wait_for_tap()


        print("About to record until you stop talking")
        await f.display.show_text("Say something...", align=Alignment.MIDDLE_CENTER)
        length = await f.microphone.save_audio_file("test-audio.wav")
        print(f"Recorded {length:01.1f} seconds: \"./test-audio.wav\"")
        await f.display.show_text(f"Recorded {length:1.1f} seconds", align=Alignment.MIDDLE_CENTER)
        await asyncio.sleep(3)
        # or get the audio directly in memory:
        await f.display.show_text("Say something else...", align=Alignment.MIDDLE_CENTER)
        audio_data = await f.microphone.record_audio(max_length_in_seconds=10)
        await f.display.show_text(f"Playing back {len(audio_data) / f.microphone.sample_rate:1.1f} seconds of audio", align=Alignment.MIDDLE_CENTER)
        # you can play back the audio on your computer
        f.microphone.play_audio(audio_data)
        # or process it using other audio handling libraries, upload to a speech-to-text service, etc.
        

        
        # let's write (or overwrite) the file greeting.txt with "Hello world".
        # You can provide a bytes object or convert a string with .encode()
        await f.files.write_file("greeting.txt", b"Hello world")

        # And now we read that file back.
        # Note that we should convert the bytearray to a string via the .decode() method.
        print((await f.files.read_file("greeting.txt")).decode())
        
        # run_lua will automatically handle scripts that are too long for the MTU, so you don't need to worry about it.
        # It will also automatically handle responses that are too long for the MTU automatically.
        await f.run_lua("frame.display.text('Hello world', 50, 100);frame.display.show()")

        # evaluate is equivalent to f.run_lua("print(\"1+2\"), await_print=True)
        # It will also automatically handle responses that are too long for the MTU automatically.
        print(await f.evaluate("1+2"))


        # take a photo and save to disk
        await f.display.show_text("Taking photo...", align=Alignment.MIDDLE_CENTER)
        await f.camera.save_photo("frame-test-photo.jpg")
        await f.display.show_text("Photo saved!", align=Alignment.MIDDLE_CENTER)
        # or with more control
        await f.camera.save_photo("frame-test-photo-2.jpg", autofocus_seconds=3, quality=f.camera.HIGH_QUALITY, autofocus_type=f.camera.AUTOFOCUS_TYPE_CENTER_WEIGHTED)
        # or get the raw bytes
        photo_bytes = await f.camera.take_photo(autofocus_seconds=1)

        # Show the full palette
        width = 640 // 4
        height = 400 // 4
        for color in range(0, 16):
            tile_x = (color % 4)
            tile_y = (color // 4)
            await f.display.draw_rect(tile_x*width+1, tile_y*height+1, width, height, color)
            await f.display.write_text(f"{color}", tile_x*width+width//2+1, tile_y*height+height//2+1)
        await f.display.show()
        
        print("Tap the Frame to continue...")
        await f.motion.wait_for_tap()

        # scroll some long text
        await f.display.scroll_text("Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you")

        max_roll = float('-inf')
        min_roll = float('inf')
        max_pitch = float('-inf')
        min_pitch = float('inf')
        
        for _ in range(10):
            direction = await f.motion.get_direction()
            if direction.roll > max_roll:
                max_roll = direction.roll
            if direction.roll < min_roll:
                min_roll = direction.roll
            if direction.pitch > max_pitch:
                max_pitch = direction.pitch
            if direction.pitch < min_pitch:
                min_pitch = direction.pitch
            print(f"Direction: roll={direction.roll} ({min_roll}-{max_roll}), \t pitch={direction.pitch} ({min_pitch}-{max_pitch})")
            await asyncio.sleep(0.5)
        
        await on_wake(f)

        # tell frame to sleep after 10 seconds
        await f.run_lua("frame.sleep(10);frame.display.text(' ',1,1);frame.display.show();frame.sleep()")


    print("disconnected")
    
    async def on_wake(f):
        # display battery indicator and time as a home screen
        batteryPercent = await f.get_battery_level()
        # select a battery fill color from the default palette based on level
        color = 2 if batteryPercent < 20 else 6 if batteryPercent < 50 else 9
        # specify the size of the battery indicator in the top-right
        batteryWidth = 150
        batteryHeight = 75
        # draw the endcap of the battery
        await f.display.draw_rect(640-30,40 + batteryHeight//2-8, 30, 16, 1)
        # draw the battery outline
        await f.display.draw_rect_filled(640-16-batteryWidth, 40-8, batteryWidth+16, batteryHeight+16, 8, 1, 15)
        # fill the battery based on level
        await f.display.draw_rect(640-8-batteryWidth, 40, int(batteryWidth * 0.01 * batteryPercent), batteryHeight, color)
        # write the battery level
        await f.display.write_text(f"{batteryPercent}%", 640-8-batteryWidth, 40, batteryWidth, batteryHeight, Alignment.MIDDLE_CENTER)
        # write the time and date in the center of the screen
        await f.display.write_text(datetime.datetime.now().strftime("%-I:%M %p\n%a, %B %d, %Y"), align=Alignment.MIDDLE_CENTER)
        # now show what we've been drawing to the buffer
        await f.display.show()

asyncio.run(main())
