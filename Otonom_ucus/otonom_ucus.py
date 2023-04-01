#!/usr/bin/env python3


import asyncio
import time
import math
from mavsdk import System
from mavsdk.offboard import (OffboardError, VelocityBodyYawspeed, VelocityNedYaw)


async def run():
    
    
    drone = System()
    #await drone.connect(system_address="udp://:14540")
    await drone.connect(system_address="serial:///dev/ttyACM0:57600")
    print("bağlantı bekleniyor")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"drone Bulundu....")
            break

    print("-- Arm Oluyor..")
    await drone.action.arm()
    print("-- Kalkıyor....")
    await drone.action.takeoff()
    await asyncio.sleep(6)
    time.sleep(6)

    print("-- Başlangıç Boktası Ayarlandı..")
    await drone.offboard.set_velocity_body(
        VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))

    print("-- Offboard Mode Başlatıldı")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Offboar mode baslatılması : \
              {error._result.result} nedeniyle hata verdi.. ")
        print("-- Motorlar Duruyor..")
        await drone.action.disarm()
        return
    
    ######################İKİNCİ GÖREV-- #####################
    print(f'ileri 4.5m ')
    for tur in range (1,5,1):
                
                for a in range (1,19,1):
                        
                        Th2=a*10.0
                        
                        Th=a*10.0*(math.pi/180.0)
                        #genlik=0.095877
                        genlik=0.25877
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*2*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.31)
                        
                        
                for b in range (19,37,1):
                        Th2=b*10.0
                        
                        Th=b*10.0*(math.pi/180.0)
                        genlik=0.12877/2.0
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.30)
                        if (b == 39):
                            for q in range (1,6,1):
                                
                                Th2=q*10.0
                                
                                Th=q*10.0*(math.pi/180.0)
                                genlik=0.25877
                                y_hiz = (-genlik*(math.cos(Th)))
                                x_hiz = (genlik*(math.sin(Th)))
                        
                                await drone.offboard.set_velocity_ned(
                                      VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                                await asyncio.sleep(0.30)

                        
                print("-- Tur Arası 0.5 Sn Ara verildi..")
                await drone.offboard.set_velocity_body(
                     VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                await asyncio.sleep(0.5)

#####-----------------------------------------------------------------------------
                
                tur=tur+1
####------------------------------------------------------------------------------
    print(f'1 metrelik yay ')
    for tur2 in range (1,2,1):
                
                for c in range (6,19,1):
                        Th2=c*10.0
                        Th=c*10.0*(math.pi/180.0)
                        #genlik=0.095877
                        genlik=0.23877
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.31)
                        
                        
                for d in range (25,37,1):
                        Th2=d*10.0
                        Th=d*10.0*(math.pi/180.0)
                        genlik=0.13877/2.0
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.20)
                        

                #print("-- Tur Arası 0.5 Sn Ara verildi..")
                await drone.offboard.set_velocity_body(
                     VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                await asyncio.sleep(0.5)

#####-----------------------------------------------------------------------------
                
                tur2=tur2+1
    print(f'asagi 2m saga')          
    for tur3 in range (1,3,1):
                
                for e in range (9,28,1):
                        Th2=e*10.0
                        Th=e*10.0*(math.pi/180.0)
                        #genlik=0.095877
                        genlik=0.25877
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.31)

                for f in range (28,37,1):
                        Th2=f*10.0
                        Th=f*10.0*(math.pi/180.0)
                        genlik=0.12877/2.0
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.30)
                        
                        
                        if (f == 36):
                            for g in range (0,9,1):
                                
                                Th2=g*10.0
                                Th=g*10.0*(math.pi/180.0)
                                genlik=0.13877/2.0
                                y_hiz = (-genlik*(math.cos(Th)))
                                x_hiz = (genlik*(math.sin(Th)))
                        
                                await drone.offboard.set_velocity_ned(
                                      VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                                await asyncio.sleep(0.30)
                        

                #print("-- Tur Arası 0.5 Sn Ara verildi..")
                await drone.offboard.set_velocity_body(
                     VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                await asyncio.sleep(0.5)

#####-----------------------------------------------------------------------------
                
                tur3=tur3+1
                
    print(f'4 metre asagi')       
    for tur4 in range (1,4,1):
                
                for h in range (18,37,1):
                        Th2=h*10.0
                        Th=h*10.0*(math.pi/180.0)
                        #genlik=0.095877
                        genlik=0.25877
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*2*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.31)
                        
                        
                for i in range (1,18,1):
                        Th2=i*10.0
                        Th=i*10.0*(math.pi/180.0)
                        genlik=0.12877/2.0
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.3)
                        
                await drone.offboard.set_velocity_body(
                    VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                await asyncio.sleep(0.5)

#####-----------------------------------------------------------------------------
                
                tur4=tur4+1
                
                
    print(f'2mlik yay ')
    for tur5 in range (1,3,1):
                
                for j in range (12,31,1):
                        Th2=j*10.0
                        Th=j*10.0*(math.pi/180.0)
                        #genlik=0.095877
                        genlik=0.25877
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.31)
                        
                        
                for k in range (31,37,1):
                        Th2=k*10.0
                        Th=k*10.0*(math.pi/180.0)
                        genlik=0.13877/2.0
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.20)
                        if (k == 36):
                            for l in range (1,12,1):
                                
                                Th2=l*10.0
                                Th=l*10.0*(math.pi/180.0)
                                genlik=0.13877/2.0
                                y_hiz = (-genlik*(math.cos(Th)))
                                x_hiz = (genlik*(math.sin(Th)))
                        
                                await drone.offboard.set_velocity_ned(
                                      VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                                await asyncio.sleep(0.20)
                
                
                
                
#####-----------------------------------------------------------------------------
                
                tur5=tur5+1
                #print("Uçgen-1 Yazılan Açı:", aci)
                #print("-- Tur Arası 0.5 Sn Ara verildi..")
                await drone.offboard.set_velocity_body(
                     VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                await asyncio.sleep(0.5)
####------------------------------------------------------------------------------
    for tur6 in range (1,3,1):
                #print(f'{tur6}. Tur Yapılıyor..')
                for m in range (9,28,1):
                        Th2=m*10.0
                        Th=m*10.0*(math.pi/180.0)
                        #genlik=0.095877
                        genlik=0.25877
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*2*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.31)
                        
                        
                for n in range (28,37,1):
                        Th2=n*10.0
                        Th=n*10.0*(math.pi/180.0)
                        genlik=0.13877/2.0
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.20)
                        if (n == 36):
                            for o in range (1,9,1):
                                
                                Th2=o*10.0
                                Th=o*10.0*(math.pi/180.0)
                                genlik=0.13877/2.0
                                y_hiz = (-genlik*(math.cos(Th)))
                                x_hiz = (genlik*(math.sin(Th)))
                        
                                await drone.offboard.set_velocity_ned(
                                      VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                                await asyncio.sleep(0.20)
                tur6=tur6+1
                #print("Uçgen-1 Yazılan Açı:", aci)
                #print("-- Tur Arası 0.5 Sn Ara verildi..")
                await drone.offboard.set_velocity_body(
                     VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                await asyncio.sleep(0.5)
    
    
    for tur7 in range (1,3,1):
                #print(f'{tur7}. Tur Yapılıyor..')
                for p in range (4,22,1):
                        Th2=p*10.0
                        Th=p*10.0*(math.pi/180.0)
                        #genlik=0.095877
                        genlik=0.25877
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.31)
                        
                        
                for r in range (22,37,1):
                        Th2=r*10.0
                        Th=r*10.0*(math.pi/180.0)
                        genlik=0.13877/2.0
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.20)
                        
                        
                        
                        
                        
                        #print("Uçgen-1 Yazılan Açı:", aci)
                #print("-- Tur Arası 0.5 Sn Ara verildi..")
                await drone.offboard.set_velocity_body(
                     VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                await asyncio.sleep(0.5)
                
                
                
                
#####-----------------------------------------------------------------------------
                
                tur7=tur7+1
    print(f'son 3.5 m ileri')          
    for tur8 in range (1,3,1):
                
                for s in range (1,18,1):
                        Th2=s*10.0
                        Th=s*10.0*(math.pi/180.0)
                        #genlik=0.095877
                        genlik=0.25877
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*2*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.31)
                        
                        
                for t in range (18,37,1):
                        Th2=t*10.0
                        Th=t*10.0*(math.pi/180.0)
                        genlik=0.12877/2.0
                        y_hiz = (-genlik*(math.cos(Th)))
                        x_hiz = (genlik*(math.sin(Th)))
                        
                        await drone.offboard.set_velocity_ned(
                              VelocityNedYaw(x_hiz, y_hiz, 0.0, Th2))
                        await asyncio.sleep(0.3)
                        
                await drone.offboard.set_velocity_body(
                    VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                await asyncio.sleep(0.5)
                        
                        
                        
                        
                        
                        
                
                
                
                
#####-----------------------------------------------------------------------------
                
                tur8=tur8+1
                
    print("Görevler Tamamlandı, drone İniyor..")
    print("-- 1 sn Bekle")
    await drone.offboard.set_velocity_body(
        VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(1)

    print("-- Offboar Mode Durdu")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Offboar mode baslatılması : \
              {error._result.result} nedeniyle hata verdi..")
    print("-- Landing")
    await drone.action.land()

if __name__ == "__main__":
    asyncio.run(run())

    



