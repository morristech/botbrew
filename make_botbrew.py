# Make the goals separately
# Just a simple python script to make pkg and print the logs if it fails

from sys import argv
from os import system

fail, success = 0, 0
disabled = [
	"package-ncurses",
	"package-libyaml",
	"package-libassuan",
	"package-python",
	"pacakage-pth",
	"package-libgcrypt",
	"package-db",
	"package-gmp",
	"package-gnutls",
	"package-nettle",
	"package-libtasn1",
	"package-libiconv",
	"package-libidn",
	"package-mpc",
	"package-mpfr",
	"package-git",
	"package-dialog",
	"package-neon",
	"package-libssh",
	"package-runit",
	"package-opkg",
	"package-patch",
	"package-w3m",
	"package-libnids",
	"package-hello",
	"package-libifaddrs",
	"package-haveged",
	"package-openssl",
	"package-vim",
	"package-ncursesw",
	"package-network-radar",
	"package-libcsploit-common",
	"package-libcares",
	"package-libpcap",
	"package-login",
	"package-make",
	"package-gc",
	"package-musl",
	"package-arpspoof",
	"package-libnet",
	"package-expat",
	"package-libgpg-error",
	"package-serf",
	"package-apr",
	"package-gdbm",
	"package-readline",
	"package-sqlite",
	"package-apr-util",
	"package-curl",
	"package-libffi",
	"package-diffutils",
	"package-bzip2",
	"package-lynx",
	"package-hostname",
	"package-zip",
	"package-android-mkbootfs",
	"package-pcre",
	"package-nmap",
	"package-tcpdump",
	"package-fusemounts",
	"package-botbrew-fundation",
	"package-autoconf",
	"package-rsync"] # Put packages name you don't want to compile...

goals = argv[1:]

for goal in goals:
	if goal not in disabled:
		print "Making %s..." % goal
		make = system("make -s %s 2> build.log" % goal)
		if make != 0: # Fail ?
			print "%s failed" % goal
			system("cat build.log") # Show the logs
			fail += 1
		else:
			success += 1

print "Failed: %s" % str(fail)
print "Succesfull: %s" % str(success)
print "Disabled: %s" % str(len(disabled))
print "Total: %s" % str(len(goals))