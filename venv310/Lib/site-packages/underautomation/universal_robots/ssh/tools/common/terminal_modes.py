import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Ssh.Tools.Common import TerminalModes as terminal_modes

class TerminalModes(int):
	TTY_OP_END = terminal_modes.TTY_OP_END
	VINTR = terminal_modes.VINTR
	VQUIT = terminal_modes.VQUIT
	VERASE = terminal_modes.VERASE
	VKILL = terminal_modes.VKILL
	VEOF = terminal_modes.VEOF
	VEOL = terminal_modes.VEOL
	VEOL2 = terminal_modes.VEOL2
	VSTART = terminal_modes.VSTART
	VSTOP = terminal_modes.VSTOP
	VSUSP = terminal_modes.VSUSP
	VDSUSP = terminal_modes.VDSUSP
	VREPRINT = terminal_modes.VREPRINT
	VWERASE = terminal_modes.VWERASE
	VLNEXT = terminal_modes.VLNEXT
	VFLUSH = terminal_modes.VFLUSH
	VSWTCH = terminal_modes.VSWTCH
	VSTATUS = terminal_modes.VSTATUS
	VDISCARD = terminal_modes.VDISCARD
	IGNPAR = terminal_modes.IGNPAR
	PARMRK = terminal_modes.PARMRK
	INPCK = terminal_modes.INPCK
	ISTRIP = terminal_modes.ISTRIP
	INLCR = terminal_modes.INLCR
	IGNCR = terminal_modes.IGNCR
	ICRNL = terminal_modes.ICRNL
	IUCLC = terminal_modes.IUCLC
	IXON = terminal_modes.IXON
	IXANY = terminal_modes.IXANY
	IXOFF = terminal_modes.IXOFF
	IMAXBEL = terminal_modes.IMAXBEL
	IUTF8 = terminal_modes.IUTF8
	ISIG = terminal_modes.ISIG
	ICANON = terminal_modes.ICANON
	XCASE = terminal_modes.XCASE
	ECHO = terminal_modes.ECHO
	ECHOE = terminal_modes.ECHOE
	ECHOK = terminal_modes.ECHOK
	ECHONL = terminal_modes.ECHONL
	NOFLSH = terminal_modes.NOFLSH
	TOSTOP = terminal_modes.TOSTOP
	IEXTEN = terminal_modes.IEXTEN
	ECHOCTL = terminal_modes.ECHOCTL
	ECHOKE = terminal_modes.ECHOKE
	PENDIN = terminal_modes.PENDIN
	OPOST = terminal_modes.OPOST
	OLCUC = terminal_modes.OLCUC
	ONLCR = terminal_modes.ONLCR
	OCRNL = terminal_modes.OCRNL
	ONOCR = terminal_modes.ONOCR
	ONLRET = terminal_modes.ONLRET
	CS7 = terminal_modes.CS7
	CS8 = terminal_modes.CS8
	PARENB = terminal_modes.PARENB
	PARODD = terminal_modes.PARODD
	TTY_OP_ISPEED = terminal_modes.TTY_OP_ISPEED
	TTY_OP_OSPEED = terminal_modes.TTY_OP_OSPEED
