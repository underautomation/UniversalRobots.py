from __future__ import annotations
import typing
from datetime import datetime, timedelta
from underautomation.universal_robots.license.license_state import LicenseState
from UnderAutomation.UniversalRobots.License import LicenseInfo as license_info
from UnderAutomation.UniversalRobots.License import LicenseState as license_state

class LicenseInfo:
	'''Information about a license key'''
	def __init__(self, licenseIdentifier: str, licenseKey: str, _internal = 0):
		'''Create a new LicenseInfo instance to retrieve informations about a pair of identifier/key This class should not be used to register your product. Please use static function RegisterLicense to specify your license.

		:param licenseIdentifier: The name of your organization (null for trial version)
		:param licenseKey: The key, associated to the identifier, supplied by UnderAutomation (null for trial version)
		'''
		if(_internal == 0):
			self._instance = license_info(licenseIdentifier, licenseKey)
		else:
			self._instance = _internal

	@property
	def is_licensed(self) -> bool:
		'''True if the license state is Licensed, Trial or ExtraTrial ; false otherwise'''
		return self._instance.IsLicensed

	@property
	def license_key(self) -> str:
		'''The license key supplied by UnderAutomation (null for trial period)'''
		return self._instance.LicenseKey

	@property
	def product(self) -> str:
		'''Commercial name of this .NET Software library'''
		return self._instance.Product

	@property
	def evaluation_days_left(self) -> int | None:
		'''Remaining days of the trial period. Null if the product is licensed. It could be negative if the trial period is ended since several days.'''
		return self._instance.EvaluationDaysLeft

	@property
	def evaluation_start_date(self) -> datetime:
		'''The date the trial period starts. If the product is licensed, the date of the library first use.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.EvaluationStartDate.Ticks // 10)

	@property
	def licensee(self) -> str:
		'''Name of your organisation'''
		return self._instance.Licensee

	@property
	def trial_period_expiration_date(self) -> datetime | None:
		'''The date the product will expire. Null if the product is licensed.'''
		return None if self._instance.TrialPeriodExpirationDate is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.TrialPeriodExpirationDate.Ticks // 10)

	@property
	def state(self) -> LicenseState:
		'''The current license state'''
		return LicenseState(int(self._instance.State))

	@property
	def product_release_date(self) -> datetime:
		'''The date this version of the product was released.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.ProductReleaseDate.Ticks // 10)

	@property
	def maintenance_years(self) -> int:
		'''Number of maintenance years included in your license'''
		return self._instance.MaintenanceYears

	@property
	def license_issued_date(self) -> datetime | None:
		'''The date you get the license'''
		return None if self._instance.LicenseIssuedDate is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.LicenseIssuedDate.Ticks // 10)

	@property
	def maintenance_expiration_date(self) -> datetime | None:
		'''The date your maintenance contract end and you no longer can use this license with newer versions.'''
		return None if self._instance.MaintenanceExpirationDate is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.MaintenanceExpirationDate.Ticks // 10)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LicenseInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
