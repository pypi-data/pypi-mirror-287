from .LibreGaming import LibreGaming
import argparse, subprocess

#Parse commandline arguments
def parse_arguments():
    parser = argparse.ArgumentParser(usage="%(prog)s <arguments>", description="Install Gaming Packages with ease",
                                     epilog="GPLv3 - Repo : https://github.com/Ahmed-Al-Balochi/LibreGaming.git")
    parser.add_argument('-g', '--gaming', action='store_true', help='Install all the Gaming Packages(Steam,Wine-Staging,Gamemode,Lutris,Heroic,MangoHud & Goverlay)')
    parser.add_argument('-b', '--basic', action='store_true', help='Install Basic Gaming Packages(Steam,Wine-Staging,Gamemode)')
    parser.add_argument('-ath', '--athenaeum', action='store_true', help='Install Athenaeum Launcher')
    parser.add_argument('-o', '--overlays', action='store_true', help='Install Mangohud & Goverlay')
    parser.add_argument('--heroic', action='store_true', help='Install Heroic Launcher')
    parser.add_argument('--lutris', action='store_true', help='Install Lutris Launcher')
    parser.add_argument('--minigalaxy', action='store_true', help='Install Minigalaxy Launcher')
    parser.add_argument('--itch', action='store_true', help='Install itch.io Launcher')
    parser.add_argument('--stl', action='store_true', help='Install Steam Tinker Launch(For Arch Linux only)')
    parser.add_argument('-v','--version', action='version', version='0.3')
    return parser.parse_args()

# Main execution
def main():
    try:
        print("""\n 
██╗     ██╗██████╗ ██████╗ ███████╗ ██████╗  █████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗ 
██║     ██║██╔══██╗██╔══██╗██╔════╝██╔════╝ ██╔══██╗████╗ ████║██║████╗  ██║██╔════╝ 
██║     ██║██████╔╝██████╔╝█████╗  ██║  ███╗███████║██╔████╔██║██║██╔██╗ ██║██║  ███╗
██║     ██║██╔══██╗██╔══██╗██╔══╝  ██║   ██║██╔══██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
███████╗██║██████╔╝██║  ██║███████╗╚██████╔╝██║  ██║██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
         \n""")
        LibreGaming_Object = LibreGaming()
        args = parse_arguments()
        if args.gaming:
            LibreGaming_Object.installAllPkgs()
        if args.basic:
            LibreGaming_Object.BasicPkgs()
        if args.overlays:
            LibreGaming_Object.Overlays()
        if args.lutris:
            LibreGaming_Object.Lutris()
        if args.heroic:
            LibreGaming_Object.Common_Pkgs_Object.Heroic()
        if args.stl:
            LibreGaming_Object.STL()
        if args.minigalaxy:
            LibreGaming_Object.Common_Pkgs_Object.Minigalaxy()
        if args.itch:
            LibreGaming_Object.Common_Pkgs_Object.itch()
        if args.athenaeum:
            LibreGaming_Object.Common_Pkgs_Object.Athenaeum()
    except KeyboardInterrupt:
        print("\nInterrupt signal received exiting...\n")
        exit(0)

if __name__ == "__main__":
    main()
