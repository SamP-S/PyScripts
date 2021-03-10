import pymem
import keyboard as input
import time

local_player_offsets = {
    # position
    "x"                 :   0x0004,
    "y"                 :   0x0008,
    "z"                 :   0x000c,
    # rotations
    "yaw"               :   0x0040,     # y_angle
    "pitch"             :   0x0044,     # x_angle
    "roll"              :   0x0048,     # z_angle
    # stats
    "speed"             :   0x0080,
    "health"            :   0x00f8,
    "vest"              :   0x00fc,
    # ammo
    "ammo_pistol"       :   0x114,
    "ammo_semi"         :   0x118,
    "ammo_shotgun"      :   0x11c,
    "ammo_smg"          :   0x120,
    "ammo_sniper"       :   0x124,
    "ammo_ar"           :   0x128,
    # reserve ammo
    "ammo_pistol_mags"  :   0x13c,
    "ammo_semi_mags"    :   0x140,
    "ammo_shotgun_mags" :   0x144,
    "ammo_smg_mags"     :   0x148,
    "ammo_sniper_mags"  :   0x14c,
    "ammo_ar_mags"      :   0x150,
    # grenades
    "ammo_grenades"     :   0x156,
    # shot timers (RPM)
    "wpn_tmr_knife"     :   0x0160,
    "wpn_tmr_pistol"    :   0x0164,
    "wpn_tmr_semi"      :   0x0168,
    "wpn_tmr_shotgun"   :   0x016c,
    "wpn_tmr_smg"       :   0x0170,
    "wpn_tmr_sniper"    :   0x0174,
    "wpn_tmr_ar"        :   0x0178,
    
    "wpn_tmr_grenade"   :   0x0180,

    "shots_fired"       :   0x01a0,
    "team_1"            :   0x0204,
    "mouse_btn_down"    :   0x0224,
    "team_2"            :   0x032c,

    "player_base"       :   0x109b74,   # offsets for local player
    "player_base_2"     :   0x509b74    # not sure why 2?
}


class ac_player:

    def __init__(self, process, local_addr):
        self.process = process
        self.local_addr = local_addr

        self.values = {
            # position
            "x"                 :   0,
            "y"                 :   0,
            "z"                 :   0,
            # rotations
            "yaw"               :   0,     # y_angle
            "pitch"             :   0,     # x_angle
            "roll"              :   0,     # z_angle
            # stats
            "speed"             :   0,
            "health"            :   100,
            "vest"              :   0,
            # ammo
            "ammo_pistol"       :   0,
            "ammo_semi"         :   0,
            "ammo_shotgun"      :   0,
            "ammo_smg"          :   0,
            "ammo_sniper"       :   0,
            "ammo_ar"           :   0,
            # reserve ammo
            "ammo_pistol_mags"  :   0,
            "ammo_semi_mags"    :   0,
            "ammo_shotgun_mags" :   0,
            "ammo_smg_mags"     :   0,
            "ammo_sniper_mags"  :   0,
            "ammo_ar_mags"      :   0,
            # grenades
            "ammo_grenades"     :   0,
            # shot timers (RPM)
            "wpn_tmr_knife"     :   0,
            "wpn_tmr_pistol"    :   0,
            "wpn_tmr_semi"      :   0,
            "wpn_tmr_shotgun"   :   0,
            "wpn_tmr_smg"       :   0,
            "wpn_tmr_sniper"    :   0,
            "wpn_tmr_ar"        :   0,
            
            "wpn_tmr_grenade"   :   0,

            "shots_fired"       :   0,
            "team_1"            :   0,
            "mouse_btn_down"    :   0,
            "team_2"            :   0,
        }

    def read(self):
        print("player_read")
        for key in local_player_offsets:
            self.values[key] = self.process.read(self.local_addr + local_player_offsets[key])
            print(key, " = ", self.values[key])

    def write(self, key, value):
        written = self.process.write(self.local_addr + local_player_offsets[key], value)
        if written == 0:
            print(key, " set to: ", value)
            self.values[key] = value
        else:
            print("ERROR: Could not set ", key)
    
    def set_health(self, health):
        print("HEALTH HACK")
        written = self.process.write(self.local_addr + local_player_offsets["health"], health)
        if written == 0:
            print("Health set to: ", health)
            self.values["health"] = health
        else:
            print("ERROR: Could not set health")

    def infinite_ammo(self):
        print("INFINITE AMMO")
        ammo_list = ["ammo_pistol", "ammo_semi", "ammo_shotgun", "ammo_smg", "ammo_sniper",
                    "ammo_ar", "ammo_pistol_mags", "ammo_semi_mags", "ammo_shotgun_mags",
                    "ammo_smg_mags", "ammo_sniper_mags", "ammo_ar_mags"]
        for key in ammo_list:
            self.write(key, 100)

    def rpm_increase(self):
        timer_list = ["wpn_tmr_knife", "wpn_tmr_pistol", "wpn_tmr_semi", "wpn_tmr_shotgun", "wpn_tmr_smg", "wpn_tmr_sniper", "wpn_tmr_ar", "wpn_tmr_grenade"]
        for key in timer_list:
            self.write(key, 0)

def main():
    print("Assult Cube Hack")
    
    keyboard = input.input_keyboard()

    # memory mananger setup
    rwm = pymem.ReadWriteMemory()
    process = rwm.get_process_by_name("ac_client.exe")
    process.open()
    print("PID: ", process.pid, ", name: ", process.name)
    # get local player address
    local_addr = process.read(0x400000 + 0x10F4F4)
    print("local_address = ", hex(local_addr))

    # get player object
    player = ac_player(process, local_addr)

    print("enter main")
    # main loop 
    while True:
        #player.read()
        alt_state = keyboard.get_async_key_state(input.key_codes["VK_MENU"])
        q_state = keyboard.get_async_key_state(input.key_codes["VK_Q"])
        h_state = keyboard.get_async_key_state(input.key_codes["VK_H"])
        a_state = keyboard.get_async_key_state(input.key_codes["VK_A"])
        isDown = input.key_state["isDown"]
        print("alt=", alt_state, " q=", q_state, " h=", h_state, " a=", a_state)
        if alt_state & isDown == isDown:
            #print("alt pressed")
            if q_state & isDown == isDown:
                print("QUIT")
                break
            if h_state & isDown == isDown:
                player.set_health(1000)
            if a_state & isDown == isDown:
                player.infinite_ammo()
        player.rpm_increase()
        player.infinite_ammo()
        player.set_health(1000)
        time.sleep(0.2)

if __name__ == "__main__":
    main()