# -----------------------------------------------------------------------------
import os
from copy import deepcopy
from nettoolkit.nettoolkit_common import *
from nettoolkit.addressing import *
from pprint import pprint

import nettoolkit.facts_finder as ff
from collections import OrderedDict

from .exec_device import Execute_Device

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------
# COMMON methods and variables defining class
# -----------------------------------------------------------------------------------------------
class Execute_Common():
	"""common methods/variables declaration in a Execute Common class

	Args:
		auth (dict): authentication parameters


	Raises:
		Exception: raise exception if any issue with authentication or connections.
	"""	

	# set authentication and default parameters
	def __init__(self, auth):
		self._add_auth_para(auth)
		self._set_defaults()

	# verify data, start capture, write logs
	def __call__(self):
		self._verifications()
		self.start()

	def _add_auth_para(self, auth):
		"""add authentication parameters to self instance
		
		Args:
			auth (dict): authentication parameters

		Returns:
			None
		"""
		if not isinstance(auth, dict):
			raise Exception(f"authentication parameters needs to be passed as dictionary")
		if not auth.get('un') or auth['un'] == '':
			raise Exception(f"authentication parameters missing with username `un`")
		if not auth.get('pw') or auth['pw'] == '':
			raise Exception(f"authentication parameters missing with password `pw`")
		if not auth.get('en') or auth['en'] == '':
			auth['en'] = auth['pw']
		self.auth = auth

	def _set_defaults(self):
		"""setting the default value for optional user input parameters
		"""		
		self.cumulative = True
		self.forced_login = True
		self.parsed_output = False
		self.CustomClass = None
		self.fg = False
		self.max_connections = 100
		self.mandatory_cmds_retries = 3
		self.missing_captures_only = False
		self.append_capture = False or self.missing_captures_only
		#
		self.cmd_exec_logs_all = OrderedDict()
		self.device_type_all = OrderedDict()
		self.failed_devices = {}

	def _verifications(self):
		"""Verification/Validation of input values
		"""
		if self.cumulative not in (True, False, 'both'):
			print(f"Invalid cumulative arument found: [{self.cumulative}]. capture-log files will not be generated." )
		if not isinstance(self.max_connections, int):
			print(f"Invalid number of `max_connections` defined [{self.max_connections}], default [100].")
			self.max_connections = 100

	## -------------- variable user inputs hook -------------- ##

	def dependent_cmds(self, custom_dynamic_cmd_class):
		"""Provide dependent commands via a class definition.  A new variable set of commands can be passed
		here using defined custom_dynamic_cmd_class class.  Defined class must have an abstract property called `cmds`. 
		which should return a new set/list of commands to be executed.  A good example of usage of it is - 
		derive the bgp neighbor ip addresses from show ip bgp summary output, and then create new set of commands to see
		advertised route for those neighbor ip addresses.  In this way no need to create a separate set of show commands for multiple
		devices, custom class will take care of generating additional show commands to see advertized routes based on neighbors 
		appear on bgp summary output. ( ofcouse, show ip bgp summary should be there in original show capture ) 		

		Args:
			custom_dynamic_cmd_class (_type_): _description_

		Raises:
			Exception: invalid input `custom_dynamic_cmd_class` for wront types
			Exception: mandatory property missing `cmds` for missing property in provided class
		"""	
		if not self.cumulative and custom_dynamic_cmd_class:
			print(f"Cumulative should be [True] or ['both'], in order to execute custom commands. Otherwise it will be skipped.")
			self.CustomClass = None
			return None
		#
		if not hasattr(custom_dynamic_cmd_class, '__class__'):
			raise Exception(f"invalid input [custom_dynamic_cmd_class],  expected instance of [class], got [{type(custom_dynamic_cmd_class)}]")
		try:
			custom_dynamic_cmd_class.cmds
		except AttributeError:
			raise Exception(f"mandatory property [cmds] is missing in provided class, please implement.")
		self.CustomClass = custom_dynamic_cmd_class


	##  -------------- Some other common functions --------------  ##

	def is_valid(self, ip):
		"""Validation function to check if provided ip is valid IPv4 or IPv6 address

		Args:
			ip (str): ipv4 or ipv6 address

		Returns:
			bool: True/False based on validation success/fail
		"""    		
		try:
			return ip and Validation(ip).version in (4, 6)
		except:
			print(f'Device Connection: {ip} :: Skipped due to bad Input')
			return False


	## -------------- generate Facts usings Facts-Finder hook -------------- ##

	def generate_facts(self, CustomDeviceFactsClass=None, foreign_keys={}):
		"""generate excel facts -clean.xlsx file using facts finder

		Args:
			CustomDeviceFactsClass (class, optional): class definition for the modification of excel facts with custom properties. Defaults to None.
			foreign_keys (dict, optional): custom keys(aka: custom columns) here in order to accept them and display in appropriate order. Defaults to {}.

		Raises:
			Exception: Invalid type: foreign_keys if recieved in format other than dict.
		"""		
		self.fg = True if self.cumulative else False
		if not self.fg and CustomDeviceFactsClass:
			print(f"Cumulative should be [True] or [`both`] in order to generate facts. Otherwise it will be skipped.")
			return None
		self.CustomDeviceFactsClass = CustomDeviceFactsClass
		if isinstance(foreign_keys, dict):
			self.foreign_keys = foreign_keys
		else:
			raise Exception(f'Invalid type: [foreign_keys]. Required [dict] got [{type(foreign_keys)}]')


	def _ff_sequence(self, ED, CustomDeviceFactsClass, foreign_keys):
		"""facts finder execution sequences, BPC

		Args:
			ED (Execute_Device): Execute_Device class instance post capture finishes
			CustomDeviceFactsClass (class): class definition for the modification of excel facts with custom properties.
			foreign_keys (_type_): custom keys(aka: custom columns) 
		"""	
		info_banner = " : INFO : Facts-Generation : "
		# -- cleate an instance --
		cleaned_fact = ff.CleanFacts(
			capture_log_file=ED.cumulative_filename, 
			capture_parsed_file=None,
			convert_to_cit=False,
			skip_txtfsm=True,
			new_suffix='-clean',
			use_cdp=False,
		)
		# ------------------------------------------------------------------------
		try:
			hn = ED.hostname
			# -- execute it --
			print(f"{hn}{info_banner}Starting Data Cleaning...")
			cleaned_fact()
			print(f"{hn}{info_banner}Data Cleaning done...")
		except:
			print(f"{hn}{info_banner}Data Cleaning failed, facts will NOT be generated !!!")
			return None
		# ------------------------------------------------------------------------
		if CustomDeviceFactsClass:
		# -- custom facts additions --
			try:
				print(f"{hn}{info_banner}starting Custom Data Modifications...")
				ADF = CustomDeviceFactsClass(cleaned_fact)
				ADF()
				ADF.write()
				print(f"{hn}{info_banner}Custom Data Modifications done...")
			except:
				print(f"{hn}{info_banner}Custom Data Modifications failed, custom facts will NOT be added !!")
				pass
		# ------------------------------------------------------------------------
		try:
			# -- rearranging tables columns --
			print(f"{hn}{info_banner}Column Rearranging..., ")
			ff.rearrange_tables(cleaned_fact.clean_file, foreign_keys=foreign_keys)
			print(f"{hn}{info_banner}Column Rearrangemnet done...")
		except:
			print(f"{hn}{info_banner}Column Rearrangemnet failed, facts columns may not be in proper order !")
			pass
		# ------------------------------------------------------------------------
		print(f"{hn}{info_banner}Facts-Generation Tasks Finished !!! {hn} !!")
		# ------------------------------------------------------------------------


	def _update_all_cmds(self, ED):
		"""update executed commands for all commands dictionary 

		Args:
			ED (Execute_Device): Device Execution object instance
		"""	
		if not ED.dev: return
		dt = ED.dev.dtype
		if not self.all_cmds.get(dt):
			self.all_cmds[dt] = []
		self.all_cmds[dt].extend(list(ED.all_cmds[dt]))

	@property
	def show_failures(self):
		"""Displays failure summary
		"""    		
		banner = f"\n! {'='*20} [ FAILED DEVICES AND REASONS ] {'='*20} !\n"
		print(banner)
		pprint(self.failed_devices)
		print(f"\n! {'='*72} !\n")

	def _execute(self, ip, cmds):
		"""execution function for a single device. hn == ip address in this case.

		Args:
			ip (str): ip address of a reachable device
		"""
		self.append_capture = self.append_capture or self.missing_captures_only
		# - capture instance -
		ED = Execute_Device(ip, 
			auth=self.auth, 
			cmds=cmds, 
			output_path=self.path, 
			cumulative=self.cumulative,
			forced_login=self.forced_login, 
			parsed_output=self.parsed_output,
			CustomClass=self.CustomClass,
			fg=self.fg,
			mandatory_cmds_retries=self.mandatory_cmds_retries,
			append_capture=self.append_capture,
			missing_captures_only=self.missing_captures_only,
		)
		###
		self.cmd_exec_logs_all[ED.hostname] = ED.cmd_exec_logs
		self.device_type_all[ED.hostname] =  ED.dev.dtype
		self.host_vs_ips[ED.hostname] = ip
		#

		# - update all cmds
		self._update_all_cmds(ED)

		# - facts generations -
		if self.fg: 
			self._ff_sequence(ED, self.CustomDeviceFactsClass, self.foreign_keys)




# -----------------------------------------------------------------------------------------------
# Execute class - capture_it - for common commands to all devices
# -----------------------------------------------------------------------------------------------

class Execute_By_Login(Multi_Execution, Execute_Common):
	"""Execute the device capture by logging in to device.

	Args:
		ip_list (set, list, tuple): set of ip addresses to be logging for capture
		auth (dict): authentication parameters ( un, pw, en)
		cmds (set, list, tuple): set of commands to be captured
		path (str): path where output(s), logs(s) should be stored.

	Properties:

		* cumulative (bool, optional): True: will store all commands output in a single file, False will store each command output in differet file. Defaults to False. and 'both' will do both.
		* forced_login (bool, optional): True: will try to ssh/login to devices even if ping respince fails. False will try to ssh/login only if ping responce was success. (default: False)
		* parsed_output (bool, optional): True: will check the captures and generate the general parsed excel file. False will omit this step. No excel will be generated in the case. (default: False)
		* max_connections (int, optional): 100: manipulate how many max number of concurrent connections to be establish. default is 100.
		* CustomClass (class): Custom class definitition to execute additional custom commands

	Raises:
		Exception: raise exception if any issue with authentication or connections.

	"""    	

	def __init__(self, ip_list, auth, cmds, path="."):
		Execute_Common.__init__(self, auth)
		self.devices = STR.to_set(ip_list) if isinstance(ip_list, str) else set(ip_list)
		self.cmds = cmds
		self.all_cmds = {}
		self.path = path
		#
		self.host_vs_ips = {}
		if not isinstance(cmds, dict):
			raise Exception("Commands are to be in proper dict format")
		#
		super().__init__(self.devices)

	def execute(self, ip):
		"""execution function for a single device. hn == ip address in this case.

		Args:
			ip (str): ip address of a reachable device
		"""
		self._execute(ip, self.cmds)




# -----------------------------------------------------------------------------------------------
# Execute class - capture_it - for selected individual commands for each device(s)
# -----------------------------------------------------------------------------------------------
class Execute_By_Individual_Commands(Multi_Execution, Execute_Common):
	"""Execute the device capture by logging in to device and running individual commands on to it.

	Args:
		auth (dict): authentication parameters ( un, pw, en)
		dev_cmd_dict: dictionary of list {device_ip:[commands list,]}
		path (str): path where output(s), logs(s) should be stored.

	Properties:

		* cumulative (bool, optional): True: will store all commands output in a single file, False will store each command output in differet file. Defaults to False. and 'both' will do both.
		* forced_login (bool, optional): True: will try to ssh/login to devices even if ping respince fails. False will try to ssh/login only if ping responce was success. (default: False)
		* parsed_output (bool, optional): True: will check the captures and generate the general parsed excel file. False will omit this step. No excel will be generated in the case. (default: False)
		* max_connections (int, optional): 100: manipulate how many max number of concurrent connections to be establish. default is 100.
		* CustomClass (class): Custom class definitition to execute additional custom commands

	Raises:
		Exception: raise exception if any issue with authentication or connections.

	"""    	

	def __init__(self, auth, dev_cmd_dict, path='.'):
		"""Initiatlize the connections for the provided iplist, authenticate with provided auth parameters, 
		and execute given commands.
		"""
		#
		Execute_Common.__init__(self, auth)
		#
		self.path = path
		self._verify_dev_cmd_dict(dev_cmd_dict)
		self._add_devices(dev_cmd_dict)
		self._set_individual_device_cmds_dict(dev_cmd_dict)
		#
		self.cmds = {}
		self.all_cmds = {}
		self.host_vs_ips ={}
		#
		super().__init__(self.devices)


	def _verify_dev_cmd_dict(self, dev_cmd_dict):
		"""Verify device commands dictionary `dev_cmd_dict` format and values. and raises Exceptions for errors.
		dev_cmd_dict dictionary keys are to be from either of non-iterable type such as (string, tuple, set).
		dev_cmd_dict dictionary values are to be from either of iterable type such as (list, set, tuple, dict).

		Args:
			dev_cmd_dict (dict): device commands dictionary

		Returns:
			None
		"""
		if not isinstance(dev_cmd_dict, dict):
			raise Exception(f"individual capture mandates [dev_cmd_dict] parameter as dictionary format")
		for ip, cmds in dev_cmd_dict.items():
			if isinstance(ip, (tuple, set)):
				for x in ip:
					if not isinstance(addressing(x), IPv4):
						raise Exception(f"[dev_cmd_dict] keys expects IPv4 addresses, received {ip}")

			if not isinstance(cmds, (list, set, tuple, dict)):
				raise Exception(f"[dev_cmd_dict] values expects iterables, received {type(cmds)}, {cmds}")

	def _add_devices(self, dev_cmd_dict):
		"""check device commands dictionary and returns set of devices

		Args:
			dev_cmd_dict (dict): device commands dictionary

		Returns:
			None
		"""
		devs = set()
		for ip, cmds in dev_cmd_dict.items():
			if isinstance(ip, (tuple, set)):
				for x in ip:
					devs.add(x.strip())
			elif isinstance(ip, str):
				devs.add(ip.strip())
		self.devices = devs

	def _set_individual_device_cmds_dict(self, dev_cmd_dict):
		"""check device commands dictionary and sets commands list for each of device

		Args:
			dev_cmd_dict (dict): device commands dictionary

		Returns:
			None
		"""
		self.dev_cmd_dict = {}
		for device in self.devices:
			device = device.strip()
			if not self.dev_cmd_dict.get(device):
				self.dev_cmd_dict[device] = set()
			for ips, cmds in dev_cmd_dict.items():
				if isinstance(ips, (tuple, set, list)):
					for ip in ips:
						ip = ip.strip()
						if device == ip:
							self._add_to(ip.strip(), cmds)
				elif isinstance(ips, str):
					ips = ips.strip()
					if device == ips:
						self._add_to(ips.strip(), cmds)

	def _add_to(self, ip, cmds):
		"""adds `cmds` to the set of commands for given ip in device commands dictionary 

		Args:
			ip (str): ip address of device
			cmds (set): set of commands to be added for ip

		Returns:
			None
		"""
		cmds = set(cmds)
		self.dev_cmd_dict[ip] = self.dev_cmd_dict[ip].union(cmds)

	def execute(self, ip):
		"""execution function for a single device. hn == ip address in this case.

		Args:
			ip (str): ip address of a reachable device
		"""
		self._execute(ip, sorted(self.dev_cmd_dict[ip]))




# -----------------------------------------------------------------------------------------------
