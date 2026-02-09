# Open3E - List of data points
- Version of general data points: 20260209
- Version of variant data points: 20260207

## Frequently used data points
A list of all presently known data points is available [below](#all-presently-known-data-points)
|  Did | ID   | Codec | Length | Unit | Further info |
| ---: | :--- | :--- | ---: | :---: | :--- |
**256**|**BusIdentification**|*O3EComplexType*|36|||
| |- BusAddress|O3EByteVal|1|||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- [DeviceProperty](## "{0: NOTHING, 1: BACKENDGATEWAY, 2: HMUMASTER, 3: HMUSLAVE, 4: MCUMASTER, 5: MCUSLAVE, 6: HMI, 7: BCU, 8: GASAIRRATIOSYSTEM, 9: ADIO, 10: DIO, 11: KNXGATEWAY, 12: BACNETGATEWAY, 13: MODBUSGATEWAY, 14: MBUS, 15: FRIWASTATION, 16: FUELCELL, 17: CSC, 18: PHOTOVOLTAIC, 19: PRODUCTIONGATEWAY, 20: DIAGNOSTICGATEWAY, 21: SDIO, 22: MTWOIO, 23: REMOTECONTROLLOCAL, 24: CLIMASENSOR, 25: TEMPERATURERADIATORVALVE, 26: UNDERFLOORHEATINGVALVE, 27: ENERGYMETER, 28: EMCUMASTER, 29: EMCUSLAVE, 30: BMCU, 31: HPMUMASTER, 32: HPMUSLAVE, 33: VCMU, 34: EHCU, 35: MZIO, 36: PBE, 37: HBMU, 38: OSME, 39: TWOSTEPPERMOTOR, 40: INVERTER, 41: SMARTROOMCONTROL, 42: VCUMASTER, 43: VCUSLAVE, 44: CANOPENIOMODULE, 45: FAN, 46: ELECTRICALPREHEATER, 47: ELECTRICALPOSTHEATER, 48: GENERICHEATPUMP, 49: HOMEENERGYMANAGEMENTSYSTEM, 50: EEBUSHUB, 51: HIO, 52: BCUSLAVE, 53: UNDERFLOORHEATINGBOX, 54: ZIGBEERANGEEXTENDER, 55: AIRQUALITYSENSOR, 56: WATERSOFTENER, 57: AIRPURIFIER, 58: CONNECTIONADAPTERSTEPPERMOTOR, 59: REFRIGERATIONFURNITURETYPE, 60: SOLARLOGGATEWAY, 61: SYSTEMCONTROLLEREMBEDDED, 62: WALLBOX, 63: APARTMENTTRANSFERSTATION, 64: DHWTS, 65: VENTILATIONUNIT}")|O3EEnum|1|||
| |- [DeviceFunction](## "{0: NOTHING, 1: BACKENDGATEWAY, 2: HMUMASTER, 3: HMUSLAVE, 4: MCUMASTER, 5: MCUSLAVE, 6: HMI, 7: BCU, 8: GASAIRRATIOSYSTEM, 9: ADIO, 10: DIO, 11: KNXGATEWAY, 12: BACNETGATEWAY, 13: MODBUSGATEWAY, 14: MBUS, 15: FRIWASTATION, 16: FUELCELL, 17: CSC, 18: PHOTOVOLTAIC, 19: PRODUCTIONGATEWAY, 20: DIAGNOSTICGATEWAY, 21: SDIO, 22: MTWOIO, 23: REMOTECONTROLLOCAL, 24: CLIMASENSOR, 25: TEMPERATURERADIATORVALVE, 26: UNDERFLOORHEATINGVALVE, 27: ENERGYMETER, 28: EMCUMASTER, 29: EMCUSLAVE, 30: BMCU, 31: HPMUMASTER, 32: HPMUSLAVE, 33: VCMU, 34: EHCU, 35: MZIO, 36: PBE, 37: HBMU, 38: OSME, 39: TWOSTEPPERMOTOR, 40: INVERTER, 41: SMARTROOMCONTROL, 42: VCUMASTER, 43: VCUSLAVE, 44: CANOPENIOMODULE, 45: FAN, 46: ELECTRICALPREHEATER, 47: ELECTRICALPOSTHEATER, 48: GENERICHEATPUMP, 49: HOMEENERGYMANAGEMENTSYSTEM, 50: EEBUSHUB, 51: HIO, 52: BCUSLAVE, 53: UNDERFLOORHEATINGBOX, 54: ZIGBEERANGEEXTENDER, 55: AIRQUALITYSENSOR, 56: WATERSOFTENER, 57: AIRPURIFIER, 58: CONNECTIONADAPTERSTEPPERMOTOR, 59: REFRIGERATIONFURNITURETYPE, 60: SOLARLOGGATEWAY, 61: SYSTEMCONTROLLEREMBEDDED, 62: WALLBOX, 63: APARTMENTTRANSFERSTATION, 64: DHWTS, 65: VENTILATIONUNIT}")|O3EEnum|1|||
| |- SW-Version|O3ESoftVers|8|||
| |- HW-Version|O3ESoftVers|8|||
| |- VIN|O3EUtf8|16|||
**266**|**ErrorDtcHistory**|*O3EList*|124|||
| |- Count|O3EByteVal|2|||
| |- GrandTotal|O3EByteVal|2|||
| |- - Error|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**268**|[**FlowTemperatureSensor**](## "Flow temperature in the primary circuit downstream from the heat generator.")|*O3EComplexType*|9||[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest#data-points-relevant-for-heat-pump-curcuit-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- [SensorStatus](## "Actual state of sensor {0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**269**|[**ReturnTemperatureSensor**](## "Flow temperature in the primary circuit upstream from the heat generator.")|*O3EComplexType*|9||[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest#data-points-relevant-for-heat-pump-curcuit-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**356**|**MainPowerSupplyValue**|O3EInt16|2|||
**927**|[**BuildingType**](## "Type of building {0: OneFamily, 1: MultiFamilyOnlyHeating, 2: MultiFamilyHeatingDomesticHotWater, 3: TownHouse}")|O3EEnum|1|||
**1006**|**TargetQuickMode**|*O3EComplexType*|4|||
| |- OpMode|O3EByteVal|1|||
| |- Required|O3EBool|1|||
| |- Unknown|RawCodec|2|||
**1006**|**TargetQuickMode**|*O3EComplexType*|3|||
| |- SetModeOneTimesHotWater|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
## All presently known data points
|  Did | ID   | Codec | Length | Unit | Further info |
| ---: | :--- | :--- | ---: | :---: | :--- |
**256**|**BusIdentification**|*O3EComplexType*|36|||
| |- BusAddress|O3EByteVal|1|||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- [DeviceProperty](## "{0: NOTHING, 1: BACKENDGATEWAY, 2: HMUMASTER, 3: HMUSLAVE, 4: MCUMASTER, 5: MCUSLAVE, 6: HMI, 7: BCU, 8: GASAIRRATIOSYSTEM, 9: ADIO, 10: DIO, 11: KNXGATEWAY, 12: BACNETGATEWAY, 13: MODBUSGATEWAY, 14: MBUS, 15: FRIWASTATION, 16: FUELCELL, 17: CSC, 18: PHOTOVOLTAIC, 19: PRODUCTIONGATEWAY, 20: DIAGNOSTICGATEWAY, 21: SDIO, 22: MTWOIO, 23: REMOTECONTROLLOCAL, 24: CLIMASENSOR, 25: TEMPERATURERADIATORVALVE, 26: UNDERFLOORHEATINGVALVE, 27: ENERGYMETER, 28: EMCUMASTER, 29: EMCUSLAVE, 30: BMCU, 31: HPMUMASTER, 32: HPMUSLAVE, 33: VCMU, 34: EHCU, 35: MZIO, 36: PBE, 37: HBMU, 38: OSME, 39: TWOSTEPPERMOTOR, 40: INVERTER, 41: SMARTROOMCONTROL, 42: VCUMASTER, 43: VCUSLAVE, 44: CANOPENIOMODULE, 45: FAN, 46: ELECTRICALPREHEATER, 47: ELECTRICALPOSTHEATER, 48: GENERICHEATPUMP, 49: HOMEENERGYMANAGEMENTSYSTEM, 50: EEBUSHUB, 51: HIO, 52: BCUSLAVE, 53: UNDERFLOORHEATINGBOX, 54: ZIGBEERANGEEXTENDER, 55: AIRQUALITYSENSOR, 56: WATERSOFTENER, 57: AIRPURIFIER, 58: CONNECTIONADAPTERSTEPPERMOTOR, 59: REFRIGERATIONFURNITURETYPE, 60: SOLARLOGGATEWAY, 61: SYSTEMCONTROLLEREMBEDDED, 62: WALLBOX, 63: APARTMENTTRANSFERSTATION, 64: DHWTS, 65: VENTILATIONUNIT}")|O3EEnum|1|||
| |- [DeviceFunction](## "{0: NOTHING, 1: BACKENDGATEWAY, 2: HMUMASTER, 3: HMUSLAVE, 4: MCUMASTER, 5: MCUSLAVE, 6: HMI, 7: BCU, 8: GASAIRRATIOSYSTEM, 9: ADIO, 10: DIO, 11: KNXGATEWAY, 12: BACNETGATEWAY, 13: MODBUSGATEWAY, 14: MBUS, 15: FRIWASTATION, 16: FUELCELL, 17: CSC, 18: PHOTOVOLTAIC, 19: PRODUCTIONGATEWAY, 20: DIAGNOSTICGATEWAY, 21: SDIO, 22: MTWOIO, 23: REMOTECONTROLLOCAL, 24: CLIMASENSOR, 25: TEMPERATURERADIATORVALVE, 26: UNDERFLOORHEATINGVALVE, 27: ENERGYMETER, 28: EMCUMASTER, 29: EMCUSLAVE, 30: BMCU, 31: HPMUMASTER, 32: HPMUSLAVE, 33: VCMU, 34: EHCU, 35: MZIO, 36: PBE, 37: HBMU, 38: OSME, 39: TWOSTEPPERMOTOR, 40: INVERTER, 41: SMARTROOMCONTROL, 42: VCUMASTER, 43: VCUSLAVE, 44: CANOPENIOMODULE, 45: FAN, 46: ELECTRICALPREHEATER, 47: ELECTRICALPOSTHEATER, 48: GENERICHEATPUMP, 49: HOMEENERGYMANAGEMENTSYSTEM, 50: EEBUSHUB, 51: HIO, 52: BCUSLAVE, 53: UNDERFLOORHEATINGBOX, 54: ZIGBEERANGEEXTENDER, 55: AIRQUALITYSENSOR, 56: WATERSOFTENER, 57: AIRPURIFIER, 58: CONNECTIONADAPTERSTEPPERMOTOR, 59: REFRIGERATIONFURNITURETYPE, 60: SOLARLOGGATEWAY, 61: SYSTEMCONTROLLEREMBEDDED, 62: WALLBOX, 63: APARTMENTTRANSFERSTATION, 64: DHWTS, 65: VENTILATIONUNIT}")|O3EEnum|1|||
| |- SW-Version|O3ESoftVers|8|||
| |- HW-Version|O3ESoftVers|8|||
| |- VIN|O3EUtf8|16|||
**257**|**StatusDtcList**|*O3EList*|122|||
| |- Count|O3EByteVal|2|||
| |- - State|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**258**|**StatusDtcHistory**|*O3EList*|122|||
| |- Count|O3EByteVal|2|||
| |- - State|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**259**|**InfoDtcList**|*O3EList*|122|||
| |- Count|O3EByteVal|2|||
| |- - Info|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**260**|**InfoDtcHistory**|*O3EList*|122|||
| |- Count|O3EByteVal|2|||
| |- - Info|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**261**|**ServiceDtcList**|*O3EList*|122|||
| |- Count|O3EByteVal|2|||
| |- - [Service](## "{0: NoServiceRequired, 1: HoursTillServiceExpired, 2: ReplaceSacrificialAnode, 4: RefillWaterSystem, 5: RegularMaintenanceActive, 6: OverhaulActive, 7: DurationOfLife, 8: BurnerOperatingHoursTillServiceExpired, 9: ServiceFuelCellSixMonthsTillServiceExpired, 10: ServiceFuelCellFiveMonthsTillServiceExpired, 11: ServiceFuelCellFourMonthsTillServiceExpired, 12: ServiceFuelCellThreeMonthsTillServiceExpired, 13: ServiceFuelCellTwoMonthTillServiceExpired, 14: ServiceFuelCellFourtyfiveDaysTillServiceExpired, 15: ServiceFuelCellOneMonthTillServiceExpired, 16: ServiceFuelCellSixMonthsTillOverhaulExpired, 17: ServiceFuelCellFiveMonthsTillOverhaulExpired, 18: ServiceFuelCellFourMonthsTillOverhaulExpired, 19: ServiceFuelCellThreeMonthsTillOverhaulExpired, 20: ServiceFuelCellTwoMonthTillOverhaulExpired, 21: ServiceFuelCellFourtyfiveDaysTillOverhaulExpired, 22: ServiceFuelCellOneMonthTillOverhaulExpired, 23: ServiceFuelCellSixMonthsTillEndOfLife, 24: ServiceFuelCellFiveMonthsTillEndOfLife, 25: ServiceFuelCellFourMonthsTillEndOfLife, 26: ServiceFuelCellThreeMonthsTillEndOfLife, 27: ServiceFuelCellTwoMonthTillEndOfLife, 28: ServiceFuelCellFourtyfiveDaysTillEndOfLife, 29: ServiceFuelCellOneMonthTillEndOfLife, 30: BalancingInProgress, 31: BackupPowerFunctionActive, 32: BatteryLow, 33: BatteryDeviceTurnedOff, 34: MaintenanceIntervalHydraulicFilterExpired, 35: MaintenanceIntervalVentilationFilterExpired, 36: ContaminationAirFilter, 37: LagDeviceDtcReported, 65533: ViewedServiceList, 65534: ServiceDoneSuccessful}")|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**262**|**ServiceDtcHistory**|*O3EList*|122|||
| |- Count|O3EByteVal|2|||
| |- - [Service](## "{0: NoServiceRequired, 1: HoursTillServiceExpired, 2: ReplaceSacrificialAnode, 4: RefillWaterSystem, 5: RegularMaintenanceActive, 6: OverhaulActive, 7: DurationOfLife, 8: BurnerOperatingHoursTillServiceExpired, 9: ServiceFuelCellSixMonthsTillServiceExpired, 10: ServiceFuelCellFiveMonthsTillServiceExpired, 11: ServiceFuelCellFourMonthsTillServiceExpired, 12: ServiceFuelCellThreeMonthsTillServiceExpired, 13: ServiceFuelCellTwoMonthTillServiceExpired, 14: ServiceFuelCellFourtyfiveDaysTillServiceExpired, 15: ServiceFuelCellOneMonthTillServiceExpired, 16: ServiceFuelCellSixMonthsTillOverhaulExpired, 17: ServiceFuelCellFiveMonthsTillOverhaulExpired, 18: ServiceFuelCellFourMonthsTillOverhaulExpired, 19: ServiceFuelCellThreeMonthsTillOverhaulExpired, 20: ServiceFuelCellTwoMonthTillOverhaulExpired, 21: ServiceFuelCellFourtyfiveDaysTillOverhaulExpired, 22: ServiceFuelCellOneMonthTillOverhaulExpired, 23: ServiceFuelCellSixMonthsTillEndOfLife, 24: ServiceFuelCellFiveMonthsTillEndOfLife, 25: ServiceFuelCellFourMonthsTillEndOfLife, 26: ServiceFuelCellThreeMonthsTillEndOfLife, 27: ServiceFuelCellTwoMonthTillEndOfLife, 28: ServiceFuelCellFourtyfiveDaysTillEndOfLife, 29: ServiceFuelCellOneMonthTillEndOfLife, 30: BalancingInProgress, 31: BackupPowerFunctionActive, 32: BatteryLow, 33: BatteryDeviceTurnedOff, 34: MaintenanceIntervalHydraulicFilterExpired, 35: MaintenanceIntervalVentilationFilterExpired, 36: ContaminationAirFilter, 37: LagDeviceDtcReported, 65533: ViewedServiceList, 65534: ServiceDoneSuccessful}")|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**263**|**WarningDtcList**|*O3EList*|122|||
| |- Count|O3EByteVal|2|||
| |- - Warning|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**264**|**WarningDtcHistory**|*O3EList*|124|||
| |- Count|O3EByteVal|2|||
| |- GrandTotal|O3EByteVal|2|||
| |- - Warning|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**265**|**ErrorDtcList**|*O3EList*|122|||
| |- Count|O3EByteVal|2|||
| |- - Error|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**266**|**ErrorDtcHistory**|*O3EList*|124|||
| |- Count|O3EByteVal|2|||
| |- GrandTotal|O3EByteVal|2|||
| |- - Error|O3EEnum|2|||
| |- - DateTime|O3EDateTime|8|||
| |- - Unknown|O3EByteVal|2|||
**268**|[**FlowTemperatureSensor**](## "Flow temperature in the primary circuit downstream from the heat generator.")|*O3EComplexType*|9||[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest#data-points-relevant-for-heat-pump-curcuit-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- [SensorStatus](## "Actual state of sensor {0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**269**|[**ReturnTemperatureSensor**](## "Flow temperature in the primary circuit upstream from the heat generator.")|*O3EComplexType*|9||[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest#data-points-relevant-for-heat-pump-curcuit-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**271**|**DomesticHotWaterSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**272**|**DomesticHotWaterFlowSensor**|RawCodec|10|||
**273**|**SolarRoofTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**274**|**OutsideTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**275**|**SolarBottomTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**277**|**BufferBottomTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**278**|**BufferMidBottomTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**279**|**BufferMidTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**281**|**BufferTopTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**282**|**HydraulicSeparatorTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**283**|**HydraulicSeparatorReturnTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**284**|**MixerOneCircuitFlowTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**285**|**MixerOneCircuitReturnTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**286**|**MixerTwoCircuitFlowTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**287**|**MixerTwoCircuitReturnTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**288**|**MixerThreeCircuitFlowTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**289**|**MixerThreeCircuitReturnTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**290**|**MixerFourCircuitFlowTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**291**|**MixerFourCircuitReturnTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**318**|**WaterPressureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**320**|**PrimaryHeatExchangerLiquidTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**321**|**CompressorInletTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**322**|**CompressorInletPressureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Unknown|O3EByteVal|1|||
**324**|**CompressorOutletTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**325**|**CompressorOutletPressureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Unknown|O3EByteVal|1|||
**327**|**OutdoorAirTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**328**|**SupplyAirTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**329**|**ExtractAirTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**330**|**ExhaustAirTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**331**|**FlueGasTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**323**|**EnhancedVapourInjectionTemperatureSensor**|RawCodec|9|||
**334**|**MixerOneCircuitRoomTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**335**|**MixerTwoCircuitRoomTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**336**|**MixerThreeCircuitRoomTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**337**|**MixerFourCircuitRoomTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**354**|**PrimaryHeatExchangerBaseHeater**|O3EByteVal|1|||
**355**|**SecondaryHeatExchangerLiquidTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**356**|**MainPowerSupplyValue**|O3EInt16|2|||
**360**|**DomesticHotWaterOutletSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**364**|**Flame**|*O3EComplexType*|6|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|2|||
| |- IonizationCurrent|O3EInt16|2|||
| |- Unknown2|RawCodec|1|||
**365**|**FlameStatistical**|*O3EComplexType*|42|||
| |- Unknown1|RawCodec|38|||
| |- BurnerStarts|O3EInt16|2|||
| |- Unknown2|RawCodec|2|||
**373**|**FanTargetSpeed**|O3EInt16|2|||
**374**|**FanCurrentSpeed**|O3EInt16|2|||
**376**|**MassFlowSensor**|*O3EComplexType*|9|||
| |- CurrentValue|O3EInt16|2|||
| |- Min|O3EInt16|2|||
| |- Max|O3EInt16|2|||
| |- DeltaT|O3EInt16|2|||
| |- State|O3EByteVal|1|||
**377**|**ViessmannIdentificationNumber**|O3EUtf8|16|||
**378**|**PointOfCommonCouplingPhaseOne**|*O3EComplexType*|4|||
| |- ActivePower|O3EInt16|2|||
| |- ReactivePower|O3EInt16|2|||
**379**|**PointOfCommonCouplingPhaseTwo**|*O3EComplexType*|4|||
| |- ActivePower|O3EInt16|2|||
| |- ReactivePower|O3EInt16|2|||
**380**|**PointOfCommonCouplingPhaseThree**|*O3EComplexType*|4|||
| |- ActivePower|O3EInt16|2|||
| |- ReactivePower|O3EInt16|2|||
**381**|**CentralHeatingPump**|*O3EComplexType*|4|||
| |- State|O3EByteVal|1|||
| |- TargetValue|O3EInt8|1|||
| |- Actual|O3EInt8|1|||
| |- Unknown|RawCodec|1|||
**382**|**UnitsAndFormats**|*O3EComplexType*|5|||
| |- [Units](## "{0: Metric, 1: Imperial}")|O3EEnum|1|||
| |- [DateFormat](## "{0: DayMonthYear, 1: MonthDayYear, 2: YearMonthDay}")|O3EEnum|1|||
| |- [TimeFormat](## "{0: TwentyFourHours, 1: TwelveHours}")|O3EEnum|1|||
| |- TimeZone|O3EByteVal|1|||
| |- Unknown|O3EByteVal|1|||
**386**|**DiverterValveTargetPosition**|O3EByteVal|1|||
**388**|**ElectronicExpansionValveOneTargetPositionPercent**|O3EInt8|1|||
**389**|**ElectronicExpansionValveOneCurrentPositionPercent**|O3EInt8|1|||
**390**|**ElectronicExpansionValveTwoTargetPositionPercent**|O3EInt8|1|||
**391**|**ElectronicExpansionValveTwoCurrentPositionPercent**|O3EInt8|1|||
**392**|**DomesticHotWaterPump**|RawCodec|4|||
**395**|**CentralHeatingTemperatureSetpoint**|O3EInt16|2|||
**396**|**DomesticHotWaterTemperatureSetpoint**|O3EInt16|2|||
**401**|**MixerOneCircuitPump**|*O3EComplexType*|5|||
| |- TargetPowerState|O3EByteVal|1|||
| |- TargetValue|O3EInt8|1|||
| |- PowerState|O3EByteVal|1|||
| |- ErrorState|O3EByteVal|1|||
| |- ActualValue|O3EInt8|1|||
**402**|**MixerTwoCircuitPump**|*O3EComplexType*|5|||
| |- TargetPowerState|O3EByteVal|1|||
| |- TargetValue|O3EInt8|1|||
| |- PowerState|O3EByteVal|1|||
| |- ErrorState|O3EByteVal|1|||
| |- ActualValue|O3EInt8|1|||
**403**|**MixerThreeCircuitPump**|*O3EComplexType*|5|||
| |- TargetPowerState|O3EByteVal|1|||
| |- TargetValue|O3EInt8|1|||
| |- PowerState|O3EByteVal|1|||
| |- ErrorState|O3EByteVal|1|||
| |- ActualValue|O3EInt8|1|||
**404**|**MixerFourCircuitPump**|*O3EComplexType*|5|||
| |- TargetPowerState|O3EByteVal|1|||
| |- TargetValue|O3EInt8|1|||
| |- PowerState|O3EByteVal|1|||
| |- ErrorState|O3EByteVal|1|||
| |- ActualValue|O3EInt8|1|||
**405**|**MixerFiveCircuitPump**|*O3EComplexType*|5|||
| |- TargetPowerState|O3EByteVal|1|||
| |- TargetValue|O3EInt8|1|||
| |- PowerState|O3EByteVal|1|||
| |- ErrorState|O3EByteVal|1|||
| |- ActualValue|O3EInt8|1|||
**406**|**MixerSixCircuitPump**|*O3EComplexType*|5|||
| |- TargetPowerState|O3EByteVal|1|||
| |- TargetValue|O3EInt8|1|||
| |- PowerState|O3EByteVal|1|||
| |- ErrorState|O3EByteVal|1|||
| |- ActualValue|O3EInt8|1|||
**407**|**MixerSevenCircuitPump**|*O3EComplexType*|5|||
| |- TargetPowerState|O3EByteVal|1|||
| |- TargetValue|O3EInt8|1|||
| |- PowerState|O3EByteVal|1|||
| |- ErrorState|O3EByteVal|1|||
| |- ActualValue|O3EInt8|1|||
**408**|**MixerEightCircuitPump**|*O3EComplexType*|5|||
| |- TargetPowerState|O3EByteVal|1|||
| |- TargetValue|O3EInt8|1|||
| |- PowerState|O3EByteVal|1|||
| |- ErrorState|O3EByteVal|1|||
| |- ActualValue|O3EInt8|1|||
**417**|**SolarCircuitPump**|*O3EComplexType*|5|||
| |- SolarCircuitPump|O3EInt8|1|||
| |- Unknown|RawCodec|4|||
**419**|**OutdoorAirHumiditySensor**|*O3EComplexType*|5|||
| |- Actual|O3EByteVal|1|||
| |- Minimum|O3EByteVal|1|||
| |- Maximum|O3EByteVal|1|||
| |- Average|O3EByteVal|1|||
| |- Error|O3EByteVal|1|||
**420**|**SupplyAirHumiditySensor**|*O3EComplexType*|5|||
| |- Actual|O3EByteVal|1|||
| |- Minimum|O3EByteVal|1|||
| |- Maximum|O3EByteVal|1|||
| |- Average|O3EByteVal|1|||
| |- Error|O3EByteVal|1|||
**421**|**ExtractAirHumiditySensor**|*O3EComplexType*|5|||
| |- Actual|O3EByteVal|1|||
| |- Minimum|O3EByteVal|1|||
| |- Maximum|O3EByteVal|1|||
| |- Average|O3EByteVal|1|||
| |- Error|O3EByteVal|1|||
**422**|**ExhaustAirHumiditySensor**|*O3EComplexType*|5|||
| |- Actual|O3EByteVal|1|||
| |- Minimum|O3EByteVal|1|||
| |- Maximum|O3EByteVal|1|||
| |- Average|O3EByteVal|1|||
| |- Error|O3EByteVal|1|||
**424**|**MixerOneCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Standard|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Increased|O3EInt16|2|||
| |- Duration|O3EByteVal|1|||
**426**|**MixerTwoCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Standard|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Increased|O3EInt16|2|||
| |- Duration|O3EByteVal|1|||
**428**|**MixerThreeCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Standard|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Increased|O3EInt16|2|||
| |- Duration|O3EByteVal|1|||
**429**|**ElectricalPreHeater**|RawCodec|4|||
**430**|**MixerFourCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Standard|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Increased|O3EInt16|2|||
| |- Duration|O3EByteVal|1|||
**431**|**SupplyAirVolumeFlowSensor**|*O3EComplexType*|9|||
| |- Zuluftvolumenstrom|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**432**|**MixerFiveCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Standard|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Increased|O3EInt16|2|||
| |- Duration|O3EByteVal|1|||
**433**|**ExhaustAirVolumeFlowSensor**|*O3EComplexType*|9|||
| |- Abluftvolumenstrom|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**434**|**MixerSixCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Standard|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Increased|O3EInt16|2|||
| |- Duration|O3EByteVal|1|||
**435**|**VentilationStageTargetVolumeFlow**|*O3EComplexType*|8|||
| |- Stage1|O3EInt16|2|||
| |- Stage2|O3EInt16|2|||
| |- Stage3|O3EInt16|2|||
| |- Stage4|O3EInt16|2|||
**436**|**MixerSevenCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Standard|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Increased|O3EInt16|2|||
| |- Duration|O3EByteVal|1|||
**437**|**BypassOperationState**|*O3EComplexType*|2|||
| |- BypassStatus|O3EByteVal|1|||
| |- Unknown1|O3EByteVal|1|||
**438**|**MixerEightCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Standard|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Increased|O3EInt16|2|||
| |- Duration|O3EByteVal|1|||
**439**|**BypassAvailableModes**|O3EByteVal|1|||
**449**|**ElectricalEnergyMatrix**|RawCodec|141|||
**451**|**ExternalAlternatingCurrentPowerSetpoint**|RawCodec|4|||
**475**|**MixerOneCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2|||
| |- Setpoint|O3EInt8|1|||
| |- Actual|O3EInt8|1|||
**476**|**MixerTwoCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2|||
| |- Setpoint|O3EInt8|1|||
| |- Actual|O3EInt8|1|||
**477**|**MixerThreeCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2|||
| |- Setpoint|O3EInt8|1|||
| |- Actual|O3EInt8|1|||
**478**|**MixerFourCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2|||
| |- Setpoint|O3EInt8|1|||
| |- Actual|O3EInt8|1|||
**491**|**DomesticHotWaterCirculationPump**|*O3EComplexType*|2|||
| |- State|O3EByteVal|1|||
| |- Unknown|O3EByteVal|1|||
**497**|**DomesticHotWaterCirculationPumpMode**|*O3EComplexType*|5|||
| |- Mode|O3EByteVal|1|||
| |- HygenieActive|O3EByteVal|1|||
| |- HeatingActive|O3EByteVal|1|||
| |- CyclesPerHour|O3EByteVal|1|||
| |- Cycles|O3EByteVal|1|||
**500**|**CentralHeatDemandExternalAc**|RawCodec|2|||
**503**|**ScaldProtection**|RawCodec|2|||
**504**|**DomesticHotWaterSetpointMetaData**|*O3EComplexType*|14|||
| |- LowerBufferLimitTemperature|O3EInt16|2|||
| |- MinimumBufferTemperature|O3EInt16|2|||
| |- DefaultBufferTemperature|O3EInt16|2|||
| |- MaximumBufferTemperature|O3EInt16|2|||
| |- UpperBufferLimitTemperature|O3EInt16|2|||
| |- EfficiencyLowerLimit|O3EInt16|2|||
| |- EfficiencyUpperLimit|O3EInt16|2|||
**505**|**Date**|O3ESdate|3|||
**506**|**Time**|O3EStime|3|||
**507**|**UniversalTimeCoordinated**|O3EUtc|4|||
**508**|**UniversalTimeCoordinatedOffset**|O3EByteVal|1|||
**510**|**Language**|O3EByteVal|1|||
**511**|**HolidayPhase**|*O3EComplexType*|8|||
| |- PhaseBegin|O3ESdate|3|||
| |- PhaseEnd|O3ESdate|3|||
| |- Planned|O3EByteVal|1|||
| |- Active|O3EByteVal|1|||
**512**|**HolidayAtHomePhase**|*O3EComplexType*|8|||
| |- PhaseBegin|O3ESdate|3|||
| |- PhaseEnd|O3ESdate|3|||
| |- Planned|O3EByteVal|1|||
| |- Active|O3EByteVal|1|||
**513**|**HolidayPhaseCircuitOne**|*O3EComplexType*|8|||
| |- PhaseBegin|O3ESdate|3|||
| |- PhaseEnd|O3ESdate|3|||
| |- Planned|O3EByteVal|1|||
| |- Active|O3EByteVal|1|||
**514**|**HolidayAtHomePhaseCircuitOne**|*O3EComplexType*|8|||
| |- PhaseBegin|O3ESdate|3|||
| |- PhaseEnd|O3ESdate|3|||
| |- Planned|O3EByteVal|1|||
| |- Active|O3EByteVal|1|||
**515**|**HolidayPhaseCircuitTwo**|*O3EComplexType*|8|||
| |- PhaseBegin|O3ESdate|3|||
| |- PhaseEnd|O3ESdate|3|||
| |- Planned|O3EByteVal|1|||
| |- Active|O3EByteVal|1|||
**516**|**HolidayAtHomePhaseCircuitTwo**|*O3EComplexType*|8|||
| |- PhaseBegin|O3ESdate|3|||
| |- PhaseEnd|O3ESdate|3|||
| |- Planned|O3EByteVal|1|||
| |- Active|O3EByteVal|1|||
**517**|**HolidayPhaseCircuitThree**|*O3EComplexType*|8|||
| |- PhaseBegin|O3ESdate|3|||
| |- PhaseEnd|O3ESdate|3|||
| |- Planned|O3EByteVal|1|||
| |- Active|O3EByteVal|1|||
**518**|**HolidayAtHomePhaseCircuitThree**|*O3EComplexType*|8|||
| |- PhaseBegin|O3ESdate|3|||
| |- PhaseEnd|O3ESdate|3|||
| |- Planned|O3EByteVal|1|||
| |- Active|O3EByteVal|1|||
**519**|**HolidayPhaseCircuitFour**|*O3EComplexType*|8|||
| |- PhaseBegin|O3ESdate|3|||
| |- PhaseEnd|O3ESdate|3|||
| |- Planned|O3EByteVal|1|||
| |- Active|O3EByteVal|1|||
**520**|**HolidayAtHomePhaseCircuitFour**|*O3EComplexType*|8|||
| |- PhaseBegin|O3ESdate|3|||
| |- PhaseEnd|O3ESdate|3|||
| |- Planned|O3EByteVal|1|||
| |- Active|O3EByteVal|1|||
**521**|**OperatingHoursTillService**|O3EInt16|2|||
**522**|**ServiceDateNext**|*O3EComplexType*|4|||
| |- Date|O3ESdate|3|||
| |- Status|O3EByteVal|1|||
**523**|**ServiceDateLast**|O3ESdate|3|||
**524**|**ModulationTargetSetpoint**|O3EInt16|2|||
**525**|**ExternalModulationSetpoint**|O3EInt16|2|||
**526**|**ModulationCurrentValue**|O3EInt16|2|||
**527**|**FlowTemperatureTargetSetpoint**|O3EInt16|2|||
**528**|**ExternalTargetFlowTemperatureSetpoint**|O3EInt16|2|||
**531**|**DomesticHotWaterOperationState**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
**533**|**VentilationTargetOperationLevel**|*O3EComplexType*|2|||
| |- Acutual|O3EByteVal|1|||
| |- Unknown1|O3EByteVal|1|||
**534**|**DomesticHotWaterPumpPostRunTime**|RawCodec|2|||
**535**|**ObjectElectricalEnergyStatistical**|*O3EComplexType*|12|||
| |- GridFeedInEnergy|O3EInt32|4|||
| |- GridSuppliedEnergy|O3EInt32|4|||
| |- ProducedEnergy|O3EInt32|4|||
**537**|**ExternalMixerOneCircuitTargetOperationMode**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
**538**|**ExternalDomesticHotWaterTargetOperationMode**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
**543**|**SmartGridReadyConsolidator**|*O3EComplexType*|4|||
| |- Unknown1|O3EByteVal|1|||
| |- OperatingStatus|O3EByteVal|1|||
| |- Unknown2|O3EByteVal|1|||
| |- Unknown3|O3EByteVal|1|||
**544**|**GasConsumptionCentralHeating**|*O3EComplexType*|12|||
| |- Today|O3EInt16|2|||
| |- Past7Days|O3EInt16|2|||
| |- CurrentMonth|O3EInt16|2|||
| |- PastMonth|O3EInt16|2|||
| |- CurrentYear|O3EInt16|2|||
| |- PastYear|O3EInt16|2|||
**545**|**GasConsumptionDomesticHotWater**|*O3EComplexType*|12|||
| |- Today|O3EInt16|2|||
| |- Past7Days|O3EInt16|2|||
| |- CurrentMonth|O3EInt16|2|||
| |- PastMonth|O3EInt16|2|||
| |- CurrentYear|O3EInt16|2|||
| |- PastYear|O3EInt16|2|||
**548**|**EnergyConsumptionCentralHeating**|*O3EComplexType*|24|||
| |- Today|O3EInt32|4|||
| |- Past7Days|O3EInt32|4|||
| |- CurrentMonth|O3EInt32|4|||
| |- PastMonth|O3EInt32|4|||
| |- CurrentYear|O3EInt32|4|||
| |- PastYear|O3EInt32|4|||
**565**|**EnergyConsumptionDomesticHotWater**|*O3EComplexType*|24|||
| |- Today|O3EInt32|4|||
| |- Past7Days|O3EInt32|4|||
| |- CurrentMonth|O3EInt32|4|||
| |- PastMonth|O3EInt32|4|||
| |- CurrentYear|O3EInt32|4|||
| |- PastYear|O3EInt32|4|||
**566**|**EnergyConsumptionCooling**|*O3EComplexType*|24|||
| |- Today|O3EInt32|4|||
| |- Past7Days|O3EInt32|4|||
| |- CurrentMonth|O3EInt32|4|||
| |- PastMonth|O3EInt32|4|||
| |- CurrentYear|O3EInt32|4|||
| |- PastYear|O3EInt32|4|||
**567**|**GeneratedElectricity**|*O3EComplexType*|24|||
| |- Today|O3EInt32|4|||
| |- Past7Days|O3EInt32|4|||
| |- CurrentMonth|O3EInt32|4|||
| |- PastMonth|O3EInt32|4|||
| |- CurrentYear|O3EInt32|4|||
| |- PastYear|O3EInt32|4|||
**568**|**CoTwoSavings**|RawCodec|24|||
**569**|**ResetSensorMinMaxAverageStatistics**|O3EByteVal|1|||
**570**|**ResetStatistics**|RawCodec|1|||
**572**|**SetDefaultValuesDate**|RawCodec|3|||
**573**|**RemoteReset**|RawCodec|2|||
**575**|**SetDeliveryStatus**|O3EByteVal|1|||
**576**|**SetDeliveryStatusDate**|O3ESdate|3|||
**580**|**SoftwareVersion**|O3ESoftVers|8|||
**581**|**HardwareVersion**|O3ESoftVers|8|||
**589**|**VentilationOperationHours**|O3EInt32|4|||
**592**|**MacAddressLan**|O3EMacAddr|6|||
**593**|**GatewayMac**|O3EMacAddr|6|||
**596**|**CentralHeatingPartLoadPercent**|O3EByteVal|1|||
**597**|**DomesticHotWaterPartLoadPercent**|O3EByteVal|1|||
**600**|**FuelCellReset**|RawCodec|3|||
**602**|**GatewayRemoteLocalNetworkStatus**|O3EByteVal|1|||
**603**|**GatewayApEnable**|O3EByteVal|1|||
**604**|**GatewayApDataSet**|*O3EComplexType*|76|||
| |- SSID_AccessPoint|O3EUtf8|32|||
| |- Password_AccessPoint|O3EUtf8|40|||
| |- IP-Address_AccessPoint|O3EIp4Addr|4|||
**607**|**GatewayRemoteIp**|*O3EComplexType*|20|||
| |- WLAN_IP-Address|O3EIp4Addr|4|||
| |- SubnetMask|O3EIp4Addr|4|||
| |- Gateway_IP-Address|O3EIp4Addr|4|||
| |- DNSServer1|O3EIp4Addr|4|||
| |- DNSServer2|O3EIp4Addr|4|||
**609**|**ProxyServer**|RawCodec|40|||
**610**|**ProxyPort**|RawCodec|2|||
**611**|**ProxyUser**|O3EUtf8|40|||
**613**|**ProxyEnabled**|O3EByteVal|1|||
**616**|**GatewayRemoteEnable**|O3EByteVal|1|||
**617**|**GatewayRemoteSsid**|O3EUtf8|72|||
**618**|**GatewayRemoteIpStatic**|O3EByteVal|1|||
**619**|**GatewayRemoteScanNetwork**|RawCodec|2|||
**620**|**DiagnosticServiceConnectionStatus**|O3EByteVal|1|||
**621**|**ObjectContactDetails**|*O3EComplexType*|181|||
| |- Name|O3EUtf8|20|||
| |- PreName|O3EUtf8|15|||
| |- Street|O3EUtf8|20|||
| |- StreetExtension|O3EUtf8|10|||
| |- ZipCode|O3EUtf8|7|||
| |- Region|O3EUtf8|15|||
| |- City|O3EUtf8|15|||
| |- Phone|O3EUtf8|16|||
| |- Mobile|O3EUtf8|16|||
| |- Email|O3EUtf8|30|||
| |- [Country](## "{0: Germany, 1: Austria, 2: France, 3: UnitedKingdom, 4: Afghanistan, 5: Albania, 6: Algeria, 7: Andorra, 8: Angola, 9: Antigua and Barbuda, 10: Argentina, 11: Armenia, 12: Australia, 13: Azerbaijan, 14: Bahamas, 15: Bahrain, 16: Bangladesh, 17: Barbados, 18: Belarus, 19: Belgium, 20: Belize, 21: Benin, 22: Bhutan, 23: Bolivia, 24: Bosnia and Herzegovina, 25: Botswana, 26: Brazil, 27: Brunei Darussalam, 28: Bulgaria, 29: Burkina Faso, 30: Burundi, 31: Cabo Verde, 32: Cambodia, 33: Cameroon, 34: Canada, 35: Central African Republic, 36: Chad, 37: Chile, 38: China, 39: Colombia, 40: Comoros, 41: Congo, 42: Antarcitc, 43: Costa Rica, 44: IvoryCoast, 45: Croatia, 46: Cuba, 47: Cyprus, 48: Czechia, 49: Denmark, 50: Djibouti, 51: Dominica, 52: Dominican Republic, 53: Ecuador, 54: Egypt, 55: El Salvador, 56: Equatorial Guinea, 57: Eritrea, 58: Estonia, 59: Eswatini, 60: Ethiopia, 61: Fiji, 62: Finland, 63: Gabon, 64: Gambia, 65: Georgia, 66: Ghana, 67: Greece, 68: Grenada, 69: Guatemala, 70: Guinea, 71: Guinea-Bissau, 72: Guyana, 73: Haiti, 74: Holy See, 75: Honduras, 76: Hungary, 77: Iceland, 78: India, 79: Indonesia, 80: Iran, 81: Iraq, 82: Ireland, 83: Israel, 84: Italy, 85: Jamaica, 86: Japan, 87: Jordan, 88: Kazakhstan, 89: Kenya, 90: Kiribati, 91: NorthKorea, 92: Korea, 93: Kuwait, 94: Kyrgyzstan, 95: Lao People's Democratic Republic, 96: Latvia, 97: Lebanon, 98: Lesotho, 99: Liberia, 100: Libya, 101: Liechtenstein, 102: Lithuania, 103: Luxembourg, 104: Macedonia, 105: Madagascar, 106: Malawi, 107: Malaysia, 108: Maldives, 109: Mali, 110: Malta, 111: Marshall Islands, 112: Mauritania, 113: Mauritius, 114: Mexico, 115: Micronesia, 116: Moldova, 117: Monaco, 118: Mongolia, 119: Montenegro, 120: Morocco, 121: Mozambique, 122: Myanmar, 123: Namibia, 124: Nauru, 125: Nepal, 126: Netherlands, 127: New Zealand, 128: Nicaragua, 129: Niger, 130: Nigeria, 131: Norway, 132: Oman, 133: Pakistan, 134: Palau, 135: Panama, 136: Papua New Guinea, 137: Paraguay, 138: Peru, 139: Philippines, 140: Poland, 141: Portugal, 142: Qatar, 143: Romania, 144: Russian Federation, 145: Rwanda, 146: Saint Kitts and Nevis, 147: Saint Lucia, 148: Saint Vincent and the Grenadines, 149: Samoa, 150: San Marino, 151: Sao Tome and Principe, 152: Saudi Arabia, 153: Senegal, 154: Serbia, 155: Seychelles, 156: Sierra Leone, 157: Singapore, 158: Slovakia, 159: Slovenia, 160: Solomon Islands, 161: Somalia, 162: South Africa, 163: South Sudan, 164: Spain, 165: Sri Lanka, 166: Sudan, 167: Suriname, 168: Sweden, 169: Switzerland, 170: Syrian Arab Republic, 171: Tajikistan, 172: Tanzania, 173: Thailand, 174: TimorLeste, 175: Togo, 176: Tonga, 177: Trinidad and Tobago, 178: Tunisia, 179: Turkey, 180: Turkmenistan, 181: Tuvalu, 182: Uganda, 183: Ukraine, 184: United Arab Emirates, 185: United States of America, 186: Uruguay, 187: Uzbekistan, 188: Vanuatu, 189: Venezuela, 190: Viet Nam, 191: Yemen, 192: Zambia, 193: Zimbabwe}")|O3EEnum|1|||
| |- IdentificationNumber|O3EUtf8|16|||
**622**|**CustomerDetails**|*O3EComplexType*|181|||
| |- Name|O3EUtf8|20|||
| |- PreName|O3EUtf8|15|||
| |- Street|O3EUtf8|20|||
| |- StreetExtension|O3EUtf8|10|||
| |- ZipCode|O3EUtf8|7|||
| |- Region|O3EUtf8|15|||
| |- City|O3EUtf8|15|||
| |- Phone|O3EUtf8|16|||
| |- Mobile|O3EUtf8|16|||
| |- Email|O3EUtf8|30|||
| |- [Country](## "{0: Germany, 1: Austria, 2: France, 3: UnitedKingdom, 4: Afghanistan, 5: Albania, 6: Algeria, 7: Andorra, 8: Angola, 9: Antigua and Barbuda, 10: Argentina, 11: Armenia, 12: Australia, 13: Azerbaijan, 14: Bahamas, 15: Bahrain, 16: Bangladesh, 17: Barbados, 18: Belarus, 19: Belgium, 20: Belize, 21: Benin, 22: Bhutan, 23: Bolivia, 24: Bosnia and Herzegovina, 25: Botswana, 26: Brazil, 27: Brunei Darussalam, 28: Bulgaria, 29: Burkina Faso, 30: Burundi, 31: Cabo Verde, 32: Cambodia, 33: Cameroon, 34: Canada, 35: Central African Republic, 36: Chad, 37: Chile, 38: China, 39: Colombia, 40: Comoros, 41: Congo, 42: Antarcitc, 43: Costa Rica, 44: IvoryCoast, 45: Croatia, 46: Cuba, 47: Cyprus, 48: Czechia, 49: Denmark, 50: Djibouti, 51: Dominica, 52: Dominican Republic, 53: Ecuador, 54: Egypt, 55: El Salvador, 56: Equatorial Guinea, 57: Eritrea, 58: Estonia, 59: Eswatini, 60: Ethiopia, 61: Fiji, 62: Finland, 63: Gabon, 64: Gambia, 65: Georgia, 66: Ghana, 67: Greece, 68: Grenada, 69: Guatemala, 70: Guinea, 71: Guinea-Bissau, 72: Guyana, 73: Haiti, 74: Holy See, 75: Honduras, 76: Hungary, 77: Iceland, 78: India, 79: Indonesia, 80: Iran, 81: Iraq, 82: Ireland, 83: Israel, 84: Italy, 85: Jamaica, 86: Japan, 87: Jordan, 88: Kazakhstan, 89: Kenya, 90: Kiribati, 91: NorthKorea, 92: Korea, 93: Kuwait, 94: Kyrgyzstan, 95: Lao People's Democratic Republic, 96: Latvia, 97: Lebanon, 98: Lesotho, 99: Liberia, 100: Libya, 101: Liechtenstein, 102: Lithuania, 103: Luxembourg, 104: Macedonia, 105: Madagascar, 106: Malawi, 107: Malaysia, 108: Maldives, 109: Mali, 110: Malta, 111: Marshall Islands, 112: Mauritania, 113: Mauritius, 114: Mexico, 115: Micronesia, 116: Moldova, 117: Monaco, 118: Mongolia, 119: Montenegro, 120: Morocco, 121: Mozambique, 122: Myanmar, 123: Namibia, 124: Nauru, 125: Nepal, 126: Netherlands, 127: New Zealand, 128: Nicaragua, 129: Niger, 130: Nigeria, 131: Norway, 132: Oman, 133: Pakistan, 134: Palau, 135: Panama, 136: Papua New Guinea, 137: Paraguay, 138: Peru, 139: Philippines, 140: Poland, 141: Portugal, 142: Qatar, 143: Romania, 144: Russian Federation, 145: Rwanda, 146: Saint Kitts and Nevis, 147: Saint Lucia, 148: Saint Vincent and the Grenadines, 149: Samoa, 150: San Marino, 151: Sao Tome and Principe, 152: Saudi Arabia, 153: Senegal, 154: Serbia, 155: Seychelles, 156: Sierra Leone, 157: Singapore, 158: Slovakia, 159: Slovenia, 160: Solomon Islands, 161: Somalia, 162: South Africa, 163: South Sudan, 164: Spain, 165: Sri Lanka, 166: Sudan, 167: Suriname, 168: Sweden, 169: Switzerland, 170: Syrian Arab Republic, 171: Tajikistan, 172: Tanzania, 173: Thailand, 174: TimorLeste, 175: Togo, 176: Tonga, 177: Trinidad and Tobago, 178: Tunisia, 179: Turkey, 180: Turkmenistan, 181: Tuvalu, 182: Uganda, 183: Ukraine, 184: United Arab Emirates, 185: United States of America, 186: Uruguay, 187: Uzbekistan, 188: Vanuatu, 189: Venezuela, 190: Viet Nam, 191: Yemen, 192: Zambia, 193: Zimbabwe}")|O3EEnum|1|||
| |- Identification Number|O3EUtf8|16|||
**623**|**ServiceEngineer**|*O3EComplexType*|181|||
| |- Name|O3EUtf8|20|||
| |- PreName|O3EUtf8|15|||
| |- Street|O3EUtf8|20|||
| |- StreetExtension|O3EUtf8|10|||
| |- ZipCode|O3EUtf8|7|||
| |- Region|O3EUtf8|15|||
| |- City|O3EUtf8|15|||
| |- Phone|O3EUtf8|16|||
| |- Mobile|O3EUtf8|16|||
| |- Email|O3EUtf8|30|||
| |- [Country](## "{0: Germany, 1: Austria, 2: France, 3: UnitedKingdom, 4: Afghanistan, 5: Albania, 6: Algeria, 7: Andorra, 8: Angola, 9: Antigua and Barbuda, 10: Argentina, 11: Armenia, 12: Australia, 13: Azerbaijan, 14: Bahamas, 15: Bahrain, 16: Bangladesh, 17: Barbados, 18: Belarus, 19: Belgium, 20: Belize, 21: Benin, 22: Bhutan, 23: Bolivia, 24: Bosnia and Herzegovina, 25: Botswana, 26: Brazil, 27: Brunei Darussalam, 28: Bulgaria, 29: Burkina Faso, 30: Burundi, 31: Cabo Verde, 32: Cambodia, 33: Cameroon, 34: Canada, 35: Central African Republic, 36: Chad, 37: Chile, 38: China, 39: Colombia, 40: Comoros, 41: Congo, 42: Antarcitc, 43: Costa Rica, 44: IvoryCoast, 45: Croatia, 46: Cuba, 47: Cyprus, 48: Czechia, 49: Denmark, 50: Djibouti, 51: Dominica, 52: Dominican Republic, 53: Ecuador, 54: Egypt, 55: El Salvador, 56: Equatorial Guinea, 57: Eritrea, 58: Estonia, 59: Eswatini, 60: Ethiopia, 61: Fiji, 62: Finland, 63: Gabon, 64: Gambia, 65: Georgia, 66: Ghana, 67: Greece, 68: Grenada, 69: Guatemala, 70: Guinea, 71: Guinea-Bissau, 72: Guyana, 73: Haiti, 74: Holy See, 75: Honduras, 76: Hungary, 77: Iceland, 78: India, 79: Indonesia, 80: Iran, 81: Iraq, 82: Ireland, 83: Israel, 84: Italy, 85: Jamaica, 86: Japan, 87: Jordan, 88: Kazakhstan, 89: Kenya, 90: Kiribati, 91: NorthKorea, 92: Korea, 93: Kuwait, 94: Kyrgyzstan, 95: Lao People's Democratic Republic, 96: Latvia, 97: Lebanon, 98: Lesotho, 99: Liberia, 100: Libya, 101: Liechtenstein, 102: Lithuania, 103: Luxembourg, 104: Macedonia, 105: Madagascar, 106: Malawi, 107: Malaysia, 108: Maldives, 109: Mali, 110: Malta, 111: Marshall Islands, 112: Mauritania, 113: Mauritius, 114: Mexico, 115: Micronesia, 116: Moldova, 117: Monaco, 118: Mongolia, 119: Montenegro, 120: Morocco, 121: Mozambique, 122: Myanmar, 123: Namibia, 124: Nauru, 125: Nepal, 126: Netherlands, 127: New Zealand, 128: Nicaragua, 129: Niger, 130: Nigeria, 131: Norway, 132: Oman, 133: Pakistan, 134: Palau, 135: Panama, 136: Papua New Guinea, 137: Paraguay, 138: Peru, 139: Philippines, 140: Poland, 141: Portugal, 142: Qatar, 143: Romania, 144: Russian Federation, 145: Rwanda, 146: Saint Kitts and Nevis, 147: Saint Lucia, 148: Saint Vincent and the Grenadines, 149: Samoa, 150: San Marino, 151: Sao Tome and Principe, 152: Saudi Arabia, 153: Senegal, 154: Serbia, 155: Seychelles, 156: Sierra Leone, 157: Singapore, 158: Slovakia, 159: Slovenia, 160: Solomon Islands, 161: Somalia, 162: South Africa, 163: South Sudan, 164: Spain, 165: Sri Lanka, 166: Sudan, 167: Suriname, 168: Sweden, 169: Switzerland, 170: Syrian Arab Republic, 171: Tajikistan, 172: Tanzania, 173: Thailand, 174: TimorLeste, 175: Togo, 176: Tonga, 177: Trinidad and Tobago, 178: Tunisia, 179: Turkey, 180: Turkmenistan, 181: Tuvalu, 182: Uganda, 183: Ukraine, 184: United Arab Emirates, 185: United States of America, 186: Uruguay, 187: Uzbekistan, 188: Vanuatu, 189: Venezuela, 190: Viet Nam, 191: Yemen, 192: Zambia, 193: Zimbabwe}")|O3EEnum|1|||
| |- Identification Number|O3EUtf8|16|||
**624**|**TechnicalSupport**|*O3EComplexType*|181|||
| |- Name|O3EUtf8|20|||
| |- PreName|O3EUtf8|15|||
| |- Street|O3EUtf8|20|||
| |- StreetExtension|O3EUtf8|10|||
| |- ZipCode|O3EUtf8|7|||
| |- Region|O3EUtf8|15|||
| |- City|O3EUtf8|15|||
| |- Phone|O3EUtf8|16|||
| |- Mobile|O3EUtf8|16|||
| |- Email|O3EUtf8|30|||
| |- [Country](## "{0: Germany, 1: Austria, 2: France, 3: UnitedKingdom, 4: Afghanistan, 5: Albania, 6: Algeria, 7: Andorra, 8: Angola, 9: Antigua and Barbuda, 10: Argentina, 11: Armenia, 12: Australia, 13: Azerbaijan, 14: Bahamas, 15: Bahrain, 16: Bangladesh, 17: Barbados, 18: Belarus, 19: Belgium, 20: Belize, 21: Benin, 22: Bhutan, 23: Bolivia, 24: Bosnia and Herzegovina, 25: Botswana, 26: Brazil, 27: Brunei Darussalam, 28: Bulgaria, 29: Burkina Faso, 30: Burundi, 31: Cabo Verde, 32: Cambodia, 33: Cameroon, 34: Canada, 35: Central African Republic, 36: Chad, 37: Chile, 38: China, 39: Colombia, 40: Comoros, 41: Congo, 42: Antarcitc, 43: Costa Rica, 44: IvoryCoast, 45: Croatia, 46: Cuba, 47: Cyprus, 48: Czechia, 49: Denmark, 50: Djibouti, 51: Dominica, 52: Dominican Republic, 53: Ecuador, 54: Egypt, 55: El Salvador, 56: Equatorial Guinea, 57: Eritrea, 58: Estonia, 59: Eswatini, 60: Ethiopia, 61: Fiji, 62: Finland, 63: Gabon, 64: Gambia, 65: Georgia, 66: Ghana, 67: Greece, 68: Grenada, 69: Guatemala, 70: Guinea, 71: Guinea-Bissau, 72: Guyana, 73: Haiti, 74: Holy See, 75: Honduras, 76: Hungary, 77: Iceland, 78: India, 79: Indonesia, 80: Iran, 81: Iraq, 82: Ireland, 83: Israel, 84: Italy, 85: Jamaica, 86: Japan, 87: Jordan, 88: Kazakhstan, 89: Kenya, 90: Kiribati, 91: NorthKorea, 92: Korea, 93: Kuwait, 94: Kyrgyzstan, 95: Lao People's Democratic Republic, 96: Latvia, 97: Lebanon, 98: Lesotho, 99: Liberia, 100: Libya, 101: Liechtenstein, 102: Lithuania, 103: Luxembourg, 104: Macedonia, 105: Madagascar, 106: Malawi, 107: Malaysia, 108: Maldives, 109: Mali, 110: Malta, 111: Marshall Islands, 112: Mauritania, 113: Mauritius, 114: Mexico, 115: Micronesia, 116: Moldova, 117: Monaco, 118: Mongolia, 119: Montenegro, 120: Morocco, 121: Mozambique, 122: Myanmar, 123: Namibia, 124: Nauru, 125: Nepal, 126: Netherlands, 127: New Zealand, 128: Nicaragua, 129: Niger, 130: Nigeria, 131: Norway, 132: Oman, 133: Pakistan, 134: Palau, 135: Panama, 136: Papua New Guinea, 137: Paraguay, 138: Peru, 139: Philippines, 140: Poland, 141: Portugal, 142: Qatar, 143: Romania, 144: Russian Federation, 145: Rwanda, 146: Saint Kitts and Nevis, 147: Saint Lucia, 148: Saint Vincent and the Grenadines, 149: Samoa, 150: San Marino, 151: Sao Tome and Principe, 152: Saudi Arabia, 153: Senegal, 154: Serbia, 155: Seychelles, 156: Sierra Leone, 157: Singapore, 158: Slovakia, 159: Slovenia, 160: Solomon Islands, 161: Somalia, 162: South Africa, 163: South Sudan, 164: Spain, 165: Sri Lanka, 166: Sudan, 167: Suriname, 168: Sweden, 169: Switzerland, 170: Syrian Arab Republic, 171: Tajikistan, 172: Tanzania, 173: Thailand, 174: TimorLeste, 175: Togo, 176: Tonga, 177: Trinidad and Tobago, 178: Tunisia, 179: Turkey, 180: Turkmenistan, 181: Tuvalu, 182: Uganda, 183: Ukraine, 184: United Arab Emirates, 185: United States of America, 186: Uruguay, 187: Uzbekistan, 188: Vanuatu, 189: Venezuela, 190: Viet Nam, 191: Yemen, 192: Zambia, 193: Zimbabwe}")|O3EEnum|1|||
| |- Identification Number|O3EUtf8|16|||
**625**|**ObjectDetails**|*O3EComplexType*|26|||
| |- Latitude|O3EInt32|4|||
| |- Longitude|O3EInt32|4|||
| |- Altitude|O3EInt16|2|||
| |- OrientationHorizontally|O3EInt16|2|||
| |- OrientationVertically|O3EInt16|2|||
| |- HeatingLoadPerSquareMeterPerYear|O3EInt16|2|||
| |- CentralHeatingCylinderSize|O3EInt16|2|||
| |- DomesticHotWaterCylinderSize|O3EInt16|2|||
| |- BufferCylinderSize|O3EInt16|2|||
| |- InstallationRoomSize|O3EInt16|2|||
| |- NitrogenOxide|O3EInt16|2|||
**627**|**CentralHeatingOneCircuitName**|O3EUtf8|40|||
**627**|**CentralHeatingOneCircuitName**|O3EUtf8|12|||
**628**|**CentralHeatingTwoCircuitName**|O3EUtf8|40|||
**628**|**CentralHeatingTwoCircuitName**|O3EUtf8|12|||
**629**|**CentralHeatingThreeCircuitName**|O3EUtf8|40|||
**629**|**CentralHeatingThreeCircuitName**|O3EUtf8|12|||
**630**|**CentralHeatingFourCircuitName**|O3EUtf8|40|||
**630**|**CentralHeatingFourCircuitName**|O3EUtf8|12|||
**631**|**CentralHeatingFiveCircuitName**|O3EUtf8|12|||
**632**|**CentralHeatingSixCircuitName**|O3EUtf8|12|||
**633**|**CentralHeatingSevenCircuitName**|O3EUtf8|12|||
**634**|**CentralHeatingEightCircuitName**|O3EUtf8|12|||
**645**|**GenericAnalogDigitalAccessoryOneModulFunction**|O3EByteVal|1|||
**646**|**GenericAnalogDigitalAccessoryTwoModulFunction**|O3EByteVal|1|||
**647**|**GenericAnalogDigitalAccessoryThreeModulFunction**|O3EByteVal|1|||
**648**|**GenericAnalogDigitalAccessoryFourModulFunction**|O3EByteVal|1|||
**649**|**GenericAnalogDigitalAccessoryFiveModulFunction**|O3EByteVal|1|||
**650**|**GenericDigitalAccessoryOneModulFunction**|O3EByteVal|1|||
**651**|**GenericDigitalAccessoryTwoModulFunction**|O3EByteVal|1|||
**652**|**GenericDigitalAccessoryThreeModulFunction**|O3EByteVal|1|||
**653**|**GenericDigitalAccessoryFourModulFunction**|O3EByteVal|1|||
**654**|**GenericDigitalAccessoryFiveModulFunction**|O3EByteVal|1|||
**680**|**EnergyMeter**|RawCodec|123|||
**691**|**DomesticHotWaterTimeScheduleMonday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**692**|**DomesticHotWaterTimeScheduleTuesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**693**|**DomesticHotWaterTimeScheduleWednesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**694**|**DomesticHotWaterTimeScheduleThursday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**695**|**DomesticHotWaterTimeScheduleFriday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**696**|**DomesticHotWaterTimeScheduleSaturday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**697**|**DomesticHotWaterTimeScheduleSunday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**726**|**DomesticHotWaterCirculationTimeScheduleMonday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**727**|**DomesticHotWaterCirculationTimeScheduleTuesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**728**|**DomesticHotWaterCirculationTimeScheduleWednesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**729**|**DomesticHotWaterCirculationTimeScheduleThursday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**730**|**DomesticHotWaterCirculationTimeScheduleFriday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**731**|**DomesticHotWaterCirculationTimeScheduleSaturday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**732**|**DomesticHotWaterCirculationTimeScheduleSunday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**761**|**MixerOneCircuitTimeScheduleMonday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**762**|**MixerOneCircuitTimeScheduleTuesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**763**|**MixerOneCircuitTimeScheduleWednesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**764**|**MixerOneCircuitTimeScheduleThursday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**765**|**MixerOneCircuitTimeScheduleFriday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**766**|**MixerOneCircuitTimeScheduleSaturday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**767**|**MixerOneCircuitTimeScheduleSunday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**768**|**MixerTwoCircuitTimeScheduleMonday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**769**|**MixerTwoCircuitTimeScheduleTuesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**770**|**MixerTwoCircuitTimeScheduleWednesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**771**|**MixerTwoCircuitTimeScheduleThursday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**772**|**MixerTwoCircuitTimeScheduleFriday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**773**|**MixerTwoCircuitTimeScheduleSaturday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**774**|**MixerTwoCircuitTimeScheduleSunday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**775**|**MixerThreeCircuitTimeScheduleMonday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**776**|**MixerThreeCircuitTimeScheduleTuesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**777**|**MixerThreeCircuitTimeScheduleWednesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**778**|**MixerThreeCircuitTimeScheduleThursday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**779**|**MixerThreeCircuitTimeScheduleFriday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**780**|**MixerThreeCircuitTimeScheduleSaturday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**781**|**MixerThreeCircuitTimeScheduleSunday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**782**|**MixerFourCircuitTimeScheduleMonday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**783**|**MixerFourCircuitTimeScheduleTuesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**784**|**MixerFourCircuitTimeScheduleWednesday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**785**|**MixerFourCircuitTimeScheduleThursday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**786**|**MixerFourCircuitTimeScheduleFriday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**787**|**MixerFourCircuitTimeScheduleSaturday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**788**|**MixerFourCircuitTimeScheduleSunday**|*O3EList*|57|||
| |- Count|O3EByteVal|1|||
| |- Schedules|*O3EComplexType*|7|||
| |- - Start|O3EStime|2|||
| |- - Stop|O3EStime|2|||
| |- - Unknown|RawCodec|2|||
| |- - Mode|O3EByteVal|1|||
**873**|**LegionellaProtectionActivation**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
**874**|**LegionellaProtectionTargetTemperatureSetpoint**|*O3EComplexType*|3|||
| |- Setpoint|O3EInt16|2|||
| |- Unknown|RawCodec|1|||
**875**|**LegionellaProtectionStartTime**|O3EStime|2|||
**876**|**LegionellaProtectionWeekday**|O3EByteVal|1|||
**877**|**LegionellaProtectionLastSuccessfulStartTime**|O3EStime|3|||
**878**|**LegionellaProtectionLastSuccessfulWeekday**|O3EByteVal|1|||
**880**|**MixerOneCircuitCentralHeatingCurve**|*O3EComplexType*|4|||
| |- Gradient|O3EInt8|1|||
| |- Level|O3EInt8|1|||
| |- BasePoint|O3EInt16|2|||
**881**|**MixerTwoCircuitCentralHeatingCurve**|*O3EComplexType*|4|||
| |- Gradient|O3EInt8|1|||
| |- Level|O3EInt8|1|||
| |- BasePoint|O3EInt16|2|||
**882**|**MixerThreeCircuitCentralHeatingCurve**|*O3EComplexType*|4|||
| |- Gradient|O3EInt8|1|||
| |- Level|O3EInt8|1|||
| |- BasePoint|O3EInt16|2|||
**883**|**MixerFourCircuitCentralHeatingCurve**|*O3EComplexType*|4|||
| |- Gradient|O3EInt8|1|||
| |- Level|O3EInt8|1|||
| |- BasePoint|O3EInt16|2|||
**884**|**MixerFiveCircuitCentralHeatingCurve**|*O3EComplexType*|4|||
| |- Gradient|O3EInt8|1|||
| |- Level|O3EInt8|1|||
| |- BasePoint|O3EInt16|2|||
**885**|**MixerSixCircuitCentralHeatingCurve**|*O3EComplexType*|4|||
| |- Gradient|O3EInt8|1|||
| |- Level|O3EInt8|1|||
| |- BasePoint|O3EInt16|2|||
**886**|**MixerSevenCircuitCentralHeatingCurve**|*O3EComplexType*|4|||
| |- Gradient|O3EInt8|1|||
| |- Level|O3EInt8|1|||
| |- BasePoint|O3EInt16|2|||
**887**|**MixerEightCircuitCentralHeatingCurve**|*O3EComplexType*|4|||
| |- Gradient|O3EInt8|1|||
| |- Level|O3EInt8|1|||
| |- BasePoint|O3EInt16|2|||
**896**|**OutsideTemperatureOffset**|O3EInt16|2|||
**897**|**ScreedDryingProfileActivation**|O3EByteVal|1|||
**898**|**RemainingFloorDryingDays**|O3EByteVal|1|||
**900**|**GatewayRemoteSignalStrength**|O3EByteVal|1|||
**901**|**ServiceManagerIsRequired**|O3EByteVal|1|||
**902**|**MalfunctionIdentification**|O3EByteVal|1|||
**903**|**DisplaySettings**|RawCodec|4|||
**905**|**ElectricalPostHeater**|RawCodec|4|||
**906**|**ExhaustFlap**|RawCodec|3|||
**907**|**UserInterfaceDefaultHomeScreen**|O3EByteVal|1|||
**908**|**ExternalFaultSignal**|O3EByteVal|1|||
**909**|**ExternalFaultSignalInput**|O3EByteVal|1|||
**912**|**DaylightSavingTimeActive**|RawCodec|5|||
**915**|**LastBackupDate**|O3ESdate|3|||
**917**|**RemoteWeatherService**|RawCodec|20|||
**918**|**TradeFairMode**|O3EByteVal|1|||
**919**|**OutsideTemperatureDampingFactor**|O3EInt16|2|||
**920**|**ThreeAxisAccelerationSensor**|RawCodec|36|||
**921**|**ExternalAccessInProgress**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
**922**|**ProductionTraceabilityByte**|O3EInt16|2|||
**923**|**RealTimeClockStatus**|RawCodec|8|||
**924**|**StartUpWizard**|O3EByteVal|1|||
**925**|**FillingVenting**|RawCodec|5|||
**927**|[**BuildingType**](## "Type of building {0: OneFamily, 1: MultiFamilyOnlyHeating, 2: MultiFamilyHeatingDomesticHotWater, 3: TownHouse}")|O3EEnum|1|||
**928**|**ElectronicTraceabilityNumber**|O3EUtf8|16|||
**929**|[**GasType**](## "{1: LLGas, 2: EGas, 3: LiquidGas}")|O3EEnum|1|||
**930**|**ExternalTargetCentralHeatingFlowSetpointMetaData**|RawCodec|10|||
**931**|**DomesticHotWaterFlowSetpointMetaData**|RawCodec|10|||
**933**|**MixerOneCircuitProperty**|*O3EComplexType*|9|||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1|||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1|||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1|||
| |- BusAddress|O3EByteVal|1|||
| |- FlowTemperatureOffset|O3EInt16|2|||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1|||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1|||
**934**|**MixerTwoCircuitProperty**|*O3EComplexType*|9|||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1|||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1|||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1|||
| |- BusAddress|O3EByteVal|1|||
| |- FlowTemperatureOffset|O3EInt16|2|||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1|||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1|||
**935**|**MixerThreeCircuitProperty**|*O3EComplexType*|9|||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1|||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1|||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1|||
| |- BusAddress|O3EByteVal|1|||
| |- FlowTemperatureOffset|O3EInt16|2|||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1|||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1|||
**936**|**MixerFourCircuitProperty**|*O3EComplexType*|9|||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1|||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1|||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1|||
| |- BusAddress|O3EByteVal|1|||
| |- FlowTemperatureOffset|O3EInt16|2|||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1|||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1|||
**937**|**MixerFiveCircuitProperty**|*O3EComplexType*|9|||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1|||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1|||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1|||
| |- BusAddress|O3EByteVal|1|||
| |- FlowTemperatureOffset|O3EInt16|2|||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1|||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1|||
**938**|**MixerSixCircuitProperty**|*O3EComplexType*|9|||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1|||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1|||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1|||
| |- BusAddress|O3EByteVal|1|||
| |- FlowTemperatureOffset|O3EInt16|2|||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1|||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1|||
**939**|**MixerSevenCircuitProperty**|*O3EComplexType*|9|||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1|||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1|||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1|||
| |- BusAddress|O3EByteVal|1|||
| |- FlowTemperatureOffset|O3EInt16|2|||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1|||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1|||
**940**|**MixerEightCircuitProperty**|*O3EComplexType*|9|||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1|||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1|||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1|||
| |- BusAddress|O3EByteVal|1|||
| |- FlowTemperatureOffset|O3EInt16|2|||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1|||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1|||
**950**|**SolarCircuitWaterFlowRate**|*O3EComplexType*|4|||
| |- FlowRate|O3EInt8|1|||
| |- Unknown|RawCodec|3|||
**951**|**SolarCircuitExtendedFunctions**|RawCodec|8|||
**952**|**HydraulicMatrix**|RawCodec|51|||
**953**|**SolarEnergyYield**|RawCodec|24|||
**954**|**BusTopologyMatrix**|*O3EList*|181|||
| |- Count|O3EInt8|1|||
| |- TopologyElement|*O3EComplexType*|36|||
| |- - NodeID|O3EByteVal|1|||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- - DeviceProperty|O3EByteVal|1|||
| |- - DeviceFunction|O3EByteVal|1|||
| |- - SW-Version|O3ESoftVers|8|||
| |- - HW-Version|O3ESoftVers|8|||
| |- - VIN|O3EUtf8|16|||
**960**|**ExhaustPipeType**|O3EByteVal|1|||
**961**|**SecurityAlgorithmNumber**|RawCodec|2|||
**962**|**BootLoaderVersion**|O3ESoftVers|8|||
**963**|**SparePartNumber**|O3EUtf8|16|||
**964**|[**ActiveDiagnosticSession**](## "{0: NotSet, 1: Default, 2: ProgrammingSession, 3: ExtendedDiagnosticSession, 4: SafetySystemDiagnosticSession, 64: ManufacturerProgramming, 65: ManufacturerDiagnostic, 96: SystemSupplier(VEG)Programming, 97: SystemSupplier(VEG)Diagnostic}")|O3EEnum|1|||
**987**|**MixerOneCircuitFlowTemperatureTargetSetpoint**|O3EInt16|2|||
**988**|**MixerTwoCircuitFlowTemperatureTargetSetpoint**|O3EInt16|2|||
**989**|**MixerThreeCircuitFlowTemperatureTargetSetpoint**|O3EInt16|2|||
**990**|**MixerFourCircuitFlowTemperatureTargetSetpoint**|O3EInt16|2|||
**1004**|[**CentralHeatingRegulationMode**](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1|||
**1006**|**TargetQuickMode**|*O3EComplexType*|4|||
| |- OpMode|O3EByteVal|1|||
| |- Required|O3EBool|1|||
| |- Unknown|RawCodec|2|||
**1006**|**TargetQuickMode**|*O3EComplexType*|3|||
| |- SetModeOneTimesHotWater|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**1007**|**CurrentQuickMode**|*O3EComplexType*|4|||
| |- OpMode|O3EByteVal|1|||
| |- Required|O3EBool|1|||
| |- Unknown|RawCodec|2|||
**1007**|**CurrentQuickMode**|*O3EComplexType*|3|||
| |- ModeOneTimesHotWater|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**1008**|**MixerOneCircuitTargetQuickMode**|RawCodec|4|||
**1008**|**MixerOneCircuitTargetQuickMode**|*O3EComplexType*|3|||
| |- SetModeParty|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**1009**|**MixerTwoCircuitTargetQuickMode**|RawCodec|4|||
**1009**|**MixerTwoCircuitTargetQuickMode**|*O3EComplexType*|3|||
| |- SetModeParty|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**1010**|**MixerThreeCircuitTargetQuickMode**|RawCodec|4|||
**1010**|**MixerThreeCircuitTargetQuickMode**|*O3EComplexType*|3|||
| |- SetModeParty|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**1011**|**MixerFourCircuitTargetQuickMode**|RawCodec|4|||
**1011**|**MixerFourCircuitTargetQuickMode**|*O3EComplexType*|3|||
| |- SetModeParty|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**1024**|**MixerOneCircuitCurrentQuickMode**|RawCodec|4|||
**1024**|**MixerOneCircuitCurrentQuickMode**|*O3EComplexType*|3|||
| |- ModeParty|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**1025**|**MixerTwoCircuitCurrentQuickMode**|RawCodec|4|||
**1025**|**MixerTwoCircuitCurrentQuickMode**|*O3EComplexType*|3|||
| |- ModeParty|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**1026**|**MixerThreeCircuitCurrentQuickMode**|RawCodec|4|||
**1026**|**MixerThreeCircuitCurrentQuickMode**|*O3EComplexType*|3|||
| |- ModeParty|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**1027**|**MixerFourCircuitCurrentQuickMode**|RawCodec|4|||
**1027**|**MixerFourCircuitCurrentQuickMode**|*O3EComplexType*|3|||
| |- ModeParty|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**1040**|**SupplyAirFan**|*O3EComplexType*|6|||
| |- Unknown1|RawCodec|3|||
| |- Actual|O3EInt16|2|||
| |- Unknown2|RawCodec|1|||
**1041**|**ExhaustAirFan**|*O3EComplexType*|6|||
| |- Unknown1|RawCodec|3|||
| |- Actual|O3EInt16|2|||
| |- Unknown2|RawCodec|1|||
**1042**|**PrimaryHeatExchangerTemperatureSensor**|RawCodec|9|||
**1043**|**AllengraSensor**|*O3EComplexType*|5|||
| |- Actual|O3EInt16|2|||
| |- Temperature|O3EInt16|2|||
| |- Unknown|RawCodec|1|||
**1044**|**SecondaryCentralHeatingPump**|RawCodec|2|||
**1047**|**TimeSeriesRecordedFlowTemperatureSensor**|RawCodec|11|||
**1084**|**FlowTemperatureMinimumMaximumLimit**|RawCodec|4|||
**1085**|**DomesticHotWaterHysteresis**|*O3EComplexType*|4|||
| |- SetpointSwitchOn|O3EInt16|2|||
| |- SetpointSwitchOff|O3EInt16|2|||
**1087**|**MaximumDomesticHotWaterLoadingTime**|*O3EComplexType*|2|||
| |- SetpointMaxOn|O3EInt8|1|||
| |- SetpointMinOff|O3EInt8|1|||
**1088**|**OutsideAirBypass**|O3EByteVal|1|||
**1089**|**InsideAirBypass**|O3EByteVal|1|||
**1090**|**EnvironmentAirQuality**|RawCodec|9|||
**1093**|**ExhaustPipeLength**|RawCodec|2|||
**1096**|**ResetEnergyManagerDataCollector**|O3EByteVal|1|||
**1097**|**ElectricityPrice**|*O3EComplexType*|20|||
| |- Unknown1|RawCodec|4|||
| |- Unknown2|RawCodec|4|||
| |- NormalRate|O3EInt32|4|||
| |- LowRate|O3EInt32|4|||
| |- Unknown3|RawCodec|4|||
**1098**|**GasProperties**|*O3EComplexType*|20|||
| |- Rate|O3EInt32|4|||
| |- Unknown|RawCodec|10|||
| |- VolumeCorrectionFactor|O3EInt16|2|||
| |- CalorificValue|O3EInt32|4|||
**1100**|**CentralHeatingPumpMinimumMaximumLimit**|*O3EComplexType*|3|||
| |- MinSpeed|O3EInt8|1|||
| |- MaxSpeed|O3EInt8|1|||
| |- Setpoint|O3EInt8|1|||
**1101**|**DomesticHotWaterPumpMinimumMaximumLimit**|*O3EComplexType*|3|||
| |- MinSpeed|O3EInt8|1|||
| |- MaxSpeed|O3EInt8|1|||
| |- Setpoint|O3EInt8|1|||
**1102**|**MixerOneCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3|||
| |- MinSpeed|O3EInt8|1|||
| |- MaxSpeed|O3EInt8|1|||
| |- Setpoint|O3EInt8|1|||
**1103**|**MixerTwoCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3|||
| |- MinSpeed|O3EInt8|1|||
| |- MaxSpeed|O3EInt8|1|||
| |- Setpoint|O3EInt8|1|||
**1104**|**MixerThreeCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3|||
| |- MinSpeed|O3EInt8|1|||
| |- MaxSpeed|O3EInt8|1|||
| |- Setpoint|O3EInt8|1|||
**1105**|**MixerFourCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3|||
| |- MinSpeed|O3EInt8|1|||
| |- MaxSpeed|O3EInt8|1|||
| |- Setpoint|O3EInt8|1|||
**1118**|**SolarCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3|||
| |- MinSpeed|O3EInt8|1|||
| |- MaxSpeed|O3EInt8|1|||
| |- Setpoint|O3EInt8|1|||
**1125**|**SolarMaximumLoadingTemperature**|O3EInt16|2|||
**1128**|**SolarStagnationHours**|O3EInt16|2|||
**1132**|**ViessmannIdentificationNumberListInternal**|*O3EComplexType*|97|||
| |- Count|O3EByteVal|1|||
| |- VIN1|O3EUtf8|16|||
| |- VIN2|O3EUtf8|16|||
| |- VIN3|O3EUtf8|16|||
| |- VIN4|O3EUtf8|16|||
| |- VIN5|O3EUtf8|16|||
| |- VIN6|O3EUtf8|16|||
**1136**|**SolarProperty**|RawCodec|4|||
**1137**|**ServiceModeActivation**|O3EByteVal|1|||
**1138**|**AccentLedBar**|RawCodec|1|||
**1139**|**CentralHeatingCurveAdaptionParameter**|*O3EComplexType*|7|||
| |- TemperatureHigh|O3EInt16|2|||
| |- TemperatureLow|O3EInt16|2|||
| |- Unknown|RawCodec|3|||
**1165**|**BackendConnectionStatus**|O3EByteVal|1|||
**1166**|**ResetDtcHistory**|RawCodec|5|||
**1167**|**ExternalDomesticHotWaterTemperatureSetpoint**|O3EInt16|2|||
**1172**|**SolarCircuitPumpStatistical**|RawCodec|14|||
**1175**|**AcknowledgeInfoAlarmMessage**|O3EByteVal|1|||
**1176**|**AcknowledgeWarningAlarmMessage**|O3EByteVal|1|||
**1177**|**AcknowledgeServiceAlarmMessage**|O3EByteVal|1|||
**1178**|**AcknowledgeErrorAlarmMessage**|O3EByteVal|1|||
**1181**|**DisplayTestMode**|O3EInt8|1|||
**1190**|**ThermalPower**|*O3EComplexType*|4|||
| |- Power|O3EInt16|2|||
| |- Unknown|RawCodec|2|||
**1191**|**FuelCellStatus**|RawCodec|1|||
**1192**|**MixerOneCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Unknown|RawCodec|6|||
**1193**|**MixerTwoCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Unknown|RawCodec|6|||
**1194**|**MixerThreeCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Unknown|RawCodec|6|||
**1195**|**MixerFourCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Unknown|RawCodec|6|||
**1196**|**MixerFiveCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Unknown|RawCodec|6|||
**1197**|**MixerSixCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Unknown|RawCodec|6|||
**1198**|**MixerSevenCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Unknown|RawCodec|6|||
**1199**|**MixerEightCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Unknown|RawCodec|6|||
**1210**|**FuelCellStatistical**|RawCodec|13|||
**1211**|**GeneratedCentralHeatingOutput**|*O3EComplexType*|24|||
| |- Today|O3EInt32|4|||
| |- Past7Days|O3EInt32|4|||
| |- CurrentMonth|O3EInt32|4|||
| |- PastMonth|O3EInt32|4|||
| |- CurrentYear|O3EInt32|4|||
| |- PastYear|O3EInt32|4|||
**1214**|**ElectricalPowerOutput**|O3EInt16|2|||
**1215**|**FuelCellState**|RawCodec|1|||
**1216**|**FuelCellStateTwo**|RawCodec|1|||
**1217**|**FuelCellGenerationMode**|RawCodec|1|||
**1218**|**FuelCellInstruction**|RawCodec|1|||
**1220**|**FuelCellMode**|RawCodec|1|||
**1221**|**FuelCellModeResult**|RawCodec|1|||
**1222**|**FuelCellRunRequest**|RawCodec|1|||
**1223**|**FuelCellRunRequestResult**|RawCodec|1|||
**1224**|**FuelCellStopRequest**|RawCodec|1|||
**1226**|**FuelCellProcessNumber**|RawCodec|1|||
**1227**|**FuelCellRequestAction**|RawCodec|1|||
**1228**|**FuelCellCompletionNotification**|RawCodec|1|||
**1229**|**FuelCellGasTypeSetting**|RawCodec|1|||
**1230**|**FuelCellCountrySetting**|RawCodec|1|||
**1231**|**FuelCellPrimaryPump**|RawCodec|4|||
**1232**|[**GenericDigitalInputConfigurationOnBoardOne**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1|||
**1233**|**GatewayRemoteVisibleOneTwo**|RawCodec|68|||
**1234**|**GatewayRemoteVisibleThreeFour**|RawCodec|68|||
**1235**|**GatewayRemoteVisibleFiveSix**|RawCodec|68|||
**1236**|**GatewayRemoteVisibleSevenEight**|RawCodec|68|||
**1237**|**GatewayRemoteVisibleNineTen**|RawCodec|68|||
**1238**|**AvailableActorSensorComponents**|RawCodec|31|||
**1239**|**ActorSensorTest**|RawCodec|2|||
**1240**|**CentralHeatingPumpMode**|O3EByteVal|1|||
**1241**|**MixerOneCircuitPumpMode**|O3EByteVal|1|||
**1242**|**MixerTwoCircuitPumpMode**|O3EByteVal|1|||
**1243**|**MixerThreeCircuitPumpMode**|O3EByteVal|1|||
**1244**|**MixerFourCircuitPumpMode**|O3EByteVal|1|||
**1263**|**DiverterValveBoilerHydraulicTower**|RawCodec|2|||
**1264**|**DiverterValveFuelCellHydraulicTower**|RawCodec|2|||
**1265**|**FanTargetSpeedMeta**|RawCodec|8|||
**1266**|**DiverterValveStatistical**|*O3EComplexType*|8|||
| |- Value1|O3EInt16|2|||
| |- Unknown|RawCodec|6|||
**1286**|**BusTopologyMatrixTwo**|*O3EList*|181|||
| |- Count|O3EInt8|1|||
| |- TopologyElement|*O3EComplexType*|36|||
| |- - NodeID|O3EByteVal|1|||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- - DeviceProperty|O3EByteVal|1|||
| |- - DeviceFunction|O3EByteVal|1|||
| |- - SW-Version|O3ESoftVers|8|||
| |- - HW-Version|O3ESoftVers|8|||
| |- - VIN|O3EUtf8|16|||
**1287**|**BusTopologyMatrixThree**|*O3EList*|181|||
| |- Count|O3EInt8|1|||
| |- TopologyElement|*O3EComplexType*|36|||
| |- - NodeID|O3EByteVal|1|||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- - DeviceProperty|O3EByteVal|1|||
| |- - DeviceFunction|O3EByteVal|1|||
| |- - SW-Version|O3ESoftVers|8|||
| |- - HW-Version|O3ESoftVers|8|||
| |- - VIN|O3EUtf8|16|||
**1288**|**BusTopologyMatrixFour**|*O3EList*|181|||
| |- Count|O3EInt8|1|||
| |- TopologyElement|*O3EComplexType*|36|||
| |- - NodeID|O3EByteVal|1|||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- - DeviceProperty|O3EByteVal|1|||
| |- - DeviceFunction|O3EByteVal|1|||
| |- - SW-Version|O3ESoftVers|8|||
| |- - HW-Version|O3ESoftVers|8|||
| |- - VIN|O3EUtf8|16|||
**1289**|**BusTopologyMatrixFive**|*O3EList*|181|||
| |- Count|O3EInt8|1|||
| |- TopologyElement|*O3EComplexType*|36|||
| |- - NodeID|O3EByteVal|1|||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1|||
| |- - DeviceProperty|O3EByteVal|1|||
| |- - DeviceFunction|O3EByteVal|1|||
| |- - SW-Version|O3ESoftVers|8|||
| |- - HW-Version|O3ESoftVers|8|||
| |- - VIN|O3EUtf8|16|||
**1290**|**DomesticHotWaterShiftLoadPump**|RawCodec|4|||
**1294**|**EnergyConsumptionCentralHeatingMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**1311**|**EnergyConsumptionDomesticHotWaterMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**1312**|**EnergyConsumptionCoolingMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**1313**|**GeneratedElectricityMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**1314**|**SolarEnergyYieldMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**1315**|**GeneratedCentralHeatingOutputMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**1316**|**EnergyConsumptionCentralHeatingYearMatrix**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**1333**|**EnergyConsumptionDomesticHotWaterYearMatrix**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**1334**|**EnergyConsumptionCoolingYearMatrix**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**1335**|**GeneratedElectricityYearMatrix**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**1336**|**SolarEnergyYieldYearMatrix**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**1337**|**GeneratedCentralHeatingOutputYearMatrix**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**1338**|**ScreedDryingProfileDefinition**|RawCodec|31|||
**1339**|**MalfunctionHeatingUnitBlocked**|O3EByteVal|1|||
**1340**|**FuelCellGeneratedHeatOutputMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**1341**|**FuelCellGeneratedHeatOutputYearMatrix**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**1342**|**GasConsumptionCentralHeatingMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**1343**|**GasConsumptionCentralHeatingYearMatrix**|*O3EComplexType*|48|||
| |- CurrentYear|*O3EList*|24|||
| |- - 01_January|O3EInt16|2|||
| |- - 02_February|O3EInt16|2|||
| |- - 03_March|O3EInt16|2|||
| |- - 04_April|O3EInt16|2|||
| |- - 05_May|O3EInt16|2|||
| |- - 06_June|O3EInt16|2|||
| |- - 07_July|O3EInt16|2|||
| |- - 08_August|O3EInt16|2|||
| |- - 09_September|O3EInt16|2|||
| |- - 10_October|O3EInt16|2|||
| |- - 11_November|O3EInt16|2|||
| |- - 12_December|O3EInt16|2|||
| |- LastYear|*O3EList*|24|||
| |- - 01_January|O3EInt16|2|||
| |- - 02_February|O3EInt16|2|||
| |- - 03_March|O3EInt16|2|||
| |- - 04_April|O3EInt16|2|||
| |- - 05_May|O3EInt16|2|||
| |- - 06_June|O3EInt16|2|||
| |- - 07_July|O3EInt16|2|||
| |- - 08_August|O3EInt16|2|||
| |- - 09_September|O3EInt16|2|||
| |- - 10_October|O3EInt16|2|||
| |- - 11_November|O3EInt16|2|||
| |- - 12_December|O3EInt16|2|||
**1344**|**GasConsumptionDomesticHotWaterMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**1345**|**GasConsumptionDomesticHotWaterYearMatrix**|*O3EComplexType*|48|||
| |- CurrentYear|*O3EList*|24|||
| |- - 01_January|O3EInt16|2|||
| |- - 02_February|O3EInt16|2|||
| |- - 03_March|O3EInt16|2|||
| |- - 04_April|O3EInt16|2|||
| |- - 05_May|O3EInt16|2|||
| |- - 06_June|O3EInt16|2|||
| |- - 07_July|O3EInt16|2|||
| |- - 08_August|O3EInt16|2|||
| |- - 09_September|O3EInt16|2|||
| |- - 10_October|O3EInt16|2|||
| |- - 11_November|O3EInt16|2|||
| |- - 12_December|O3EInt16|2|||
| |- LastYear|*O3EList*|24|||
| |- - 01_January|O3EInt16|2|||
| |- - 02_February|O3EInt16|2|||
| |- - 03_March|O3EInt16|2|||
| |- - 04_April|O3EInt16|2|||
| |- - 05_May|O3EInt16|2|||
| |- - 06_June|O3EInt16|2|||
| |- - 07_July|O3EInt16|2|||
| |- - 08_August|O3EInt16|2|||
| |- - 09_September|O3EInt16|2|||
| |- - 10_October|O3EInt16|2|||
| |- - 11_November|O3EInt16|2|||
| |- - 12_December|O3EInt16|2|||
**1346**|**HeatEngineStatistical**|*O3EComplexType*|12|||
| |- OperatingHours|O3EInt32|4|||
| |- BurnerHours|O3EInt32|4|||
| |- BurnerStarts|O3EInt32|4|||
**1347**|**ObjectElectricalEnergyStatus**|RawCodec|10|||
**1348**|**FuelCellGasConsumption**|*O3EComplexType*|12|||
| |- Today|O3EInt16|2|||
| |- Week|O3EInt16|2|||
| |- CurrentMonth|O3EInt16|2|||
| |- PastMonth|O3EInt16|2|||
| |- CurrentYear|O3EInt16|2|||
| |- PastYear|O3EInt16|2|||
**1349**|**FuelCellGasConsumptionMonthMatrix**|RawCodec|124|||
**1350**|**FuelCellGasConsumptionYearMatrix**|RawCodec|48|||
**1351**|**FeedInEnergy**|RawCodec|24|||
**1352**|**FeedInEnergyMonthMatrix**|RawCodec|124|||
**1353**|**FeedInEnergyYearMatrix**|RawCodec|96|||
**1354**|**ProductionCoverageRate**|RawCodec|6|||
**1355**|**ProductionCoverageRateMonthMatrix**|RawCodec|62|||
**1356**|**ProductionCoverageRateYearMatrix**|RawCodec|24|||
**1357**|**FuelCellOperationTime**|RawCodec|11|||
**1358**|**FuelCellOperationTimeMonthMatrix**|RawCodec|124|||
**1359**|**FuelCellOperationTimeYearMatrix**|RawCodec|48|||
**1360**|**FuelCellRunTime**|RawCodec|11|||
**1361**|**FuelCellRunTimeMonthMatrix**|RawCodec|124|||
**1362**|**FuelCellRunTimeYearMatrix**|RawCodec|48|||
**1363**|**FuelCellTargetOperationMode**|RawCodec|1|||
**1364**|**GenericSdioAccessoryOneModulFunction**|O3EByteVal|1|||
**1367**|**FuelCellThermalPower**|O3EInt16|2|||
**1371**|**DemandCoverageRate**|RawCodec|6|||
**1372**|**DemandCoverageRateMonthMatrix**|RawCodec|62|||
**1373**|**DemandCoverageRateYearMatrix**|RawCodec|24|||
**1383**|**FuelCellBreakdownRate**|RawCodec|11|||
**1384**|**FuelCellBreakdownRateMonthMatrix**|RawCodec|124|||
**1385**|**FuelCellBreakdownRateYearMatrix**|RawCodec|48|||
**1389**|**CoTwoSavingsMonthMatrix**|RawCodec|124|||
**1390**|**CoTwoSavingsYearMatrix**|RawCodec|96|||
**1391**|**GeneratedDomesticHotWaterOutput**|*O3EComplexType*|24|||
| |- Today|O3EInt32|4|||
| |- Past7Days|O3EInt32|4|||
| |- CurrentMonth|O3EInt32|4|||
| |- PastMonth|O3EInt32|4|||
| |- CurrentYear|O3EInt32|4|||
| |- PastYear|O3EInt32|4|||
**1392**|**GeneratedDomesticHotWaterOutputMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**1393**|**GeneratedDomesticHotWaterOutputYearMatrix**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**1394**|**SolarChargingDomesticHotWaterSetpoint**|O3EInt16|2|||
**1395**|**MixerOneCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3|||
| |- State|O3EByteVal|1|||
| |- Temperature|O3EInt16|2|||
**1396**|**MixerTwoCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3|||
| |- State|O3EByteVal|1|||
| |- Temperature|O3EInt16|2|||
**1397**|**MixerThreeCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3|||
| |- State|O3EByteVal|1|||
| |- Temperature|O3EInt16|2|||
**1398**|**MixerFourCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3|||
| |- State|O3EByteVal|1|||
| |- Temperature|O3EInt16|2|||
**1411**|**ResetServiceInterval**|O3EByteVal|1|||
**1415**|**MixerOneCircuitOperationState**|*O3EComplexType*|2|||
| |- [Mode](## "{0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**1416**|**MixerTwoCircuitOperationState**|*O3EComplexType*|2|||
| |- [Mode](## "{0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**1417**|**MixerThreeCircuitOperationState**|*O3EComplexType*|2|||
| |- [Mode](## "{0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**1418**|**MixerFourCircuitOperationState**|*O3EComplexType*|2|||
| |- [Mode](## "{0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**1419**|**MixerFiveCircuitOperationState**|*O3EComplexType*|2|||
| |- [Mode](## "{0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**1420**|**MixerSixCircuitOperationState**|*O3EComplexType*|2|||
| |- [Mode](## "{0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**1421**|**MixerSevenCircuitOperationState**|*O3EComplexType*|2|||
| |- [Mode](## "{0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**1422**|**MixerEightCircuitOperationState**|*O3EComplexType*|2|||
| |- [Mode](## "{0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**1431**|**CarbonEmissionSettings**|RawCodec|8|||
**1432**|**CentralHeatingPumpPerformance**|*O3EComplexType*|4|||
| |- Unknown|RawCodec|2|||
| |- ResidualHead|O3EByteVal|1|||
| |- DifferentialPressure|O3EByteVal|1|||
**1434**|**ResetFuelCellStatistics**|RawCodec|1|||
**1435**|**FluelCellFlowTemperatueSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**1436**|**FuelCellReturnTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**1439**|**NoiseReductionTimeScheduleMonday**|RawCodec|41|||
**1440**|**NoiseReductionTimeScheduleTuesday**|RawCodec|41|||
**1441**|**NoiseReductionTimeScheduleWednesday**|RawCodec|41|||
**1442**|**NoiseReductionTimeScheduleThursday**|RawCodec|41|||
**1443**|**NoiseReductionTimeScheduleFriday**|RawCodec|41|||
**1444**|**NoiseReductionTimeScheduleSaturday**|RawCodec|41|||
**1445**|**NoiseReductionTimeScheduleSunday**|RawCodec|41|||
**1451**|**ApplicationChecksum**|RawCodec|4|||
**1467**|**SafetyRelevantRemoteUnlock**|RawCodec|2|||
**1468**|**FuelCellGasPressure**|RawCodec|9|||
**1469**|**SensorActuatorTestGroupHeatEngine**|RawCodec|31|||
**1470**|**SensorActuatorTestGroupDomesticHotWater**|RawCodec|31|||
**1471**|**SensorActuatorTestGroupFuelCell**|RawCodec|31|||
**1472**|**SensorActuatorTestGroupHeatingCircuit**|RawCodec|31|||
**1473**|**SensorActuatorTestGroupSolar**|RawCodec|31|||
**1492**|**SolarCircuitPumpHysteresis**|RawCodec|4|||
**1493**|**HeatEnginePerformanceStatistics**|*O3EComplexType*|16|||
| |- HoursLoadClassOne|O3EInt32|4|||
| |- HoursLoadClassTwo|O3EInt32|4|||
| |- HoursLoadClassThree|O3EInt32|4|||
| |- HoursLoadClassFour|O3EInt32|4|||
**1494**|**OemProductVersion**|O3ESoftVers|8|||
**1503**|**MinimumLoadPercent**|RawCodec|1|||
**1504**|[**TimeSettingSource**](## "{0: Local, 1: SuperordinateSystem, 2: NetworkTimeProtocol, 3: TCU}")|O3EEnum|1|||
**1505**|**SolarStagnationTemperatureOffset**|RawCodec|2|||
**1529**|**SolarRechargeSuppressionImpact**|O3EByteVal|1|||
**1533**|**InstallationWizardInProgress**|RawCodec|2|||
**1535**|**FlueGasSensorTestMode**|RawCodec|3|||
**1536**|**PrimaryCircuitWaterFlowTestMode**|RawCodec|3|||
**1537**|**ChimneySweeperTestMode**|RawCodec|3|||
**1538**|**ZigbeeEnable**|O3EByteVal|1|||
**1539**|**ZigbeeStatus**|O3EByteVal|1|||
**1540**|**ZigbeeIdentification**|RawCodec|26|||
**1541**|**LegionellaProtectionPump**|RawCodec|5|||
**1549**|**HydraulicMatrixConfiguration**|RawCodec|97|||
**1550**|**FunctionMatrix**|RawCodec|22|||
**1551**|**FuelCellExternalControl**|RawCodec|1|||
**1552**|**ElectricalEnergyStorageOperationState**|RawCodec|7|||
**1553**|**ElectronicControlUnitOdxVersion**|RawCodec|6|||
**1554**|**HeatingSupport**|RawCodec|2|||
**1555**|**MixerOneCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6|||
**1556**|**MixerTwoCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6|||
**1557**|**MixerThreeCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6|||
**1558**|**MixerFourCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6|||
**1559**|**MixerFiveCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6|||
**1560**|**MixerSixCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6|||
**1561**|**MixerSevenCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6|||
**1562**|**MixerEightCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6|||
**1573**|**SystemReturnTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**1577**|**ElectricalEnergyStorageModuleOneOperatingData**|RawCodec|139|||
**1578**|**ElectricalEnergyStorageModuleTwoOperatingData**|RawCodec|139|||
**1579**|**ElectricalEnergyStorageModuleThreeOperatingData**|RawCodec|139|||
**1580**|**ElectricalEnergyStorageModuleFourOperatingData**|RawCodec|139|||
**1581**|**ElectricalEnergyStorageModuleFiveOperatingData**|RawCodec|139|||
**1582**|**ElectricalEnergyStorageModuleSixOperatingData**|RawCodec|139|||
**1585**|**IncreasedReturnTemperatureSetpoint**|RawCodec|2|||
**1587**|**ExternalAlternatingCurrentPowerSetpointMetaData**|RawCodec|4|||
**1588**|**AlternatingCurrentPowerSetpoint**|RawCodec|4|||
**1589**|**AlternatingCurrentPowerSetpointMetaData**|RawCodec|4|||
**1590**|**ElectricalEnergySystemOperationState**|RawCodec|6|||
**1591**|**ElectricalEnergyInverterOperationState**|RawCodec|6|||
**1592**|**ElectricalEnergyInverterPath**|RawCodec|1|||
**1593**|**BufferHysteresis**|RawCodec|4|||
**1594**|**LastApplicationUpdate**|O3ESdate|3|||
**1595**|**ParameterIdentificationVersionFactory**|RawCodec|8|||
**1596**|**IncreasedReturnTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- Error|O3EByteVal|1|||
**1598**|**SolarStaticTemperatureControlHysteresis**|RawCodec|4|||
**1599**|**SolarSecondaryDeltaTemperatureHysteresis**|RawCodec|4|||
**1600**|**BufferDischargeFunctionThreeWayValvePositionPercent**|RawCodec|2|||
**1601**|**FuelCellCondition**|RawCodec|1|||
**1603**|**PointOfCommonCouplingPower**|*O3EComplexType*|4|||
| |- ActivePower|O3EInt16|2|||
| |- ReactivePower|O3EInt16|2|||
**1603**|**PointOfCommonCouplingPower**|*O3EComplexType*|12|||
| |- ActivePower|O3EInt16|2|||
| |- ReactivePower|O3EInt16|2|||
| |- ActivePowerDup|O3EInt16|2|||
| |- PadZeros|O3EInt16|2|||
| |- ReactivePowerDup|O3EInt16|2|||
| |- PadOnes|O3EInt16|2|||
**1604**|**GatewayExternalTargetFlowTemperatureSetpoint**|RawCodec|2|||
**1605**|**GatewayExternalHeatEngineTargetOperationMode**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
**1606**|**IntervalStrategyProperties**|*O3EComplexType*|8|||
| |- State|O3EByteVal|1|||
| |- unknown|RawCodec|1|||
| |- BurnerOffMinTime|O3EInt16|2|||
| |- BurnerOffMaxTime|O3EInt16|2|||
| |- IntegralValue|O3EInt16|2|||
**1607**|**MalfunctionUnitBlocked**|O3EByteVal|1|||
**1608**|**DifferentialTemperatureControllerHeatSourceTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**1609**|**DifferentialTemperatureControllerHeatSinkTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**1610**|**HeatingSupportBufferTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**1611**|**PreheatingReferenceTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**1612**|**ExternalMixerTwoCircuitTargetOperationMode**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
**1613**|**ExternalMixerThreeCircuitTargetOperationMode**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
**1614**|**ExternalMixerFourCircuitTargetOperationMode**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
**1627**|**ExternalMixerOneCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2|||
**1628**|**ExternalMixerTwoCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2|||
**1629**|**ExternalMixerThreeCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2|||
**1630**|**ExternalMixerFourCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2|||
**1643**|**MixerOneCircuitCurrentTemperatureSetpoint**|O3EInt16|2|||
**1644**|**MixerTwoCircuitCurrentTemperatureSetpoint**|O3EInt16|2|||
**1645**|**MixerThreeCircuitCurrentTemperatureSetpoint**|O3EInt16|2|||
**1646**|**MixerFourCircuitCurrentTemperatureSetpoint**|O3EInt16|2|||
**1659**|**EndResultDomesticHotWaterTemperatureSetpoint**|*O3EComplexType*|3|||
| |- Setpoint|O3EInt16|2|||
| |- Unknown|RawCodec|1|||
**1660**|**SupportedFeatures**|RawCodec|16|||
**1661**|**SolarSecondaryTransferPump**|RawCodec|5|||
**1662**|**HeatingSupportBufferThreeWayValvePositionPercent**|RawCodec|2|||
**1663**|**TestStatus**|RawCodec|41|||
**1664**|**ElectricalEnergyStorageStateOfCharge**|O3EInt8|1|||
**1667**|**MixerOneCircuitPumpOscillationTime**|RawCodec|2|||
**1668**|**MixerTwoCircuitPumpOscillationTime**|RawCodec|2|||
**1669**|**MixerThreeCircuitPumpOscillationTime**|RawCodec|2|||
**1670**|**MixerFourCircuitPumpOscillationTime**|RawCodec|2|||
**1684**|**AmbientTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**1685**|**ElectricalEnergyInverterDCConfiguration**|RawCodec|3|||
**1686**|**ElectricalEnergySystemPhotovoltaicLimitation**|RawCodec|3|||
**1687**|**ElectricalEnergySystemPhotovoltaicConfiguration**|O3EInt16|2|||
**1690**|**ElectricalEnergySystemPhotovoltaicStatus**|*O3EComplexType*|17|||
| |- ActivePower cumulated|O3EInt16|2|||
| |- RectivePower cumulated|O3EInt16|2|||
| |- ActivePower String C|O3EInt16|2|||
| |- RectivePower String C|O3EInt16|2|||
| |- ActivePower String B|O3EInt16|2|||
| |- RectivePower String B|O3EInt16|2|||
| |- ActivePower String A|O3EInt16|2|||
| |- RectivePower String A|O3EInt16|2|||
| |- OpMode|O3EInt8|1|||
**1691**|**BusTopologyScanStatus**|O3EByteVal|1|||
**1692**|**PowerGridCodeConfiguration**|RawCodec|1|||
**1693**|**GridOperatorConfigurationLock**|O3EByteVal|1|||
**1694**|**GatewayEthernetEnable**|O3EByteVal|1|||
**1695**|**GatewayEthernetConfig**|RawCodec|21|||
**1696**|**GatewayEthernetIp**|RawCodec|20|||
**1697**|**GatewayEthernetNetworkStatus**|O3EByteVal|1|||
**1698**|**SupportedFeaturesTelemetryControlUnit**|RawCodec|16|||
**1699**|**ActivatedFeaturesTelemetryControlUnit**|RawCodec|16|||
**1700**|**EebusDeviceList**|RawCodec|104|||
**1701**|**EebusOwnInfo**|RawCodec|104|||
**1702**|**EebusPartnerInfo**|RawCodec|104|||
**1703**|**EebusConnectionStatus**|RawCodec|1|||
**1706**|**GenericMZIOAccessoryTwoModuleFunction**|RawCodec|1|||
**1710**|**FunctionalSoftwareVersion**|O3ESoftVers|8|||
**1718**|**ElectricalEnergySystemConfiguration**|*O3EComplexType*|2|||
| |- Netzbetriebsart|O3EByteVal|1|||
| |- Elektrische Anlagenkomponenten|O3EByteVal|1|||
**1719**|**SolarIntervalFunction**|RawCodec|3|||
**1721**|**WaterPressureConfiguration**|RawCodec|8|||
**1728**|**ThermostatTerminalOneCircuitPump**|RawCodec|2|||
**1729**|**ThermostatTerminalTwoCircuitPump**|RawCodec|2|||
**1730**|**ThermostatTerminalThreeCircuitPump**|RawCodec|2|||
**1731**|**ExternalLockActive**|O3EByteVal|1|||
**1732**|**FixedRoomTemperatureSetpoint**|RawCodec|6|||
**1749**|**TimeSeriesRecordedModulationCurrentValueStepsAndDurationOne**|RawCodec|176|||
**1750**|**TimeSeriesRecordedModulationCurrentValueStepsAndDurationTwo**|RawCodec|176|||
**1751**|**TimeSeriesRecordedModulationCurrentValueStepsAndDurationThree**|RawCodec|132|||
**1752**|**TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationOne**|RawCodec|176|||
**1753**|**TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationTwo**|RawCodec|176|||
**1754**|**TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationThree**|RawCodec|132|||
**1759**|**TimeSeriesRecordedDomesticHotWaterOutletTemperature**|RawCodec|40|||
**1760**|**TimeSeriesRecordedCombustionAirInletTemperature**|RawCodec|40|||
**1761**|**TimeSeriesRecordedCentralHeatingPumpSpeed**|RawCodec|40|||
**1762**|**LowWaterCutOffSignalInput**|RawCodec|1|||
**1763**|**LowGasPressureSignalInput**|RawCodec|1|||
**1764**|**HighGasPressureSignalInput**|RawCodec|1|||
**1765**|**CombustionAirInterlock**|RawCodec|2|||
**1766**|**ElectricalEnergyStorageModuleOperatingData**|RawCodec|141|||
**1768**|**ReceiverTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**1769**|**PrimaryInletTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**1770**|**SecondaryOutletTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**1771**|**EngineRoomTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**1772**|**CompressorOilTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**1773**|**RefrigerantCircuitFourWayValve**|O3EByteVal|1|||
**1774**|**CompressorCrankCaseHeater**|O3EByteVal|1|||
**1775**|**PrimaryCircuitFanOne**|O3EByteVal|1|||
**1776**|**PrimaryCircuitFanTwo**|O3EByteVal|1|||
**1777**|**TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationOne**|RawCodec|176|||
**1778**|**TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationTwo**|RawCodec|176|||
**1779**|**TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationThree**|RawCodec|132|||
**1780**|**TimeSeriesRecordedIgnitionTimeSteps**|RawCodec|80|||
**1781**|**TimeSeriesRecordedCalibrationCount**|RawCodec|16|||
**1782**|**TimeSeriesRecordedMonitoringIonizationMaximum**|RawCodec|56|||
**1783**|**TimeSeriesRecordedHeatingBurnerStopEvents**|RawCodec|120|||
**1784**|**TimeSeriesRecordedDomesticHotWaterBurnerStopEvents**|RawCodec|120|||
**1785**|**TimeSeriesRecordedFlameLossModulation**|RawCodec|40|||
**1786**|**TimeSeriesRecordedWaterPressureStagnation**|RawCodec|52|||
**1787**|**TimeSeriesRecordedWaterPressurePeaks**|RawCodec|32|||
**1788**|**CanInterfaceVersion**|RawCodec|8|||
**1791**|**DiverterValveDefaultPositionConfiguration**|O3EByteVal|1|||
**1792**|**ResetElectricalEnergyHistory**|RawCodec|1|||
**1793**|**BurnerPreconditions**|RawCodec|1|||
**1794**|**HeatingCircuitHeatDeficit**|RawCodec|4|||
**1795**|**FuelCellRuntimePrediction**|O3EInt8|1|||
**1796**|**DomesticElectricalEnergyConsumption**|RawCodec|2|||
**1797**|**PredictionDomesticElectricalEnergyConsumptionNextHour**|RawCodec|2|||
**1798**|**FuelCellHoursTillNextStart**|O3EInt8|1|||
**1799**|**PrimaryCircuitCurrentTemperatureSetpoint**|O3EInt16|2|||
**1800**|**ResetTimeSeriesRecordingGroups**|RawCodec|4|||
**1801**|**ElectricalEnergyStorageEnergyTransferStatistic**|*O3EComplexType*|40|||
| |- BatteryChargeToday|O3EInt32|4|||
| |- BatteryChargeWeek|O3EInt32|4|||
| |- BatteryChargeMonth|O3EInt32|4|||
| |- BatteryChargeYear|O3EInt32|4|||
| |- BatteryChargeTotal|O3EInt32|4|||
| |- BatteryDischargeToday|O3EInt32|4|||
| |- BatteryDischargeWeek|O3EInt32|4|||
| |- BatteryDischargeMonth|O3EInt32|4|||
| |- BatteryDischargeYear|O3EInt32|4|||
| |- BatteryDischargeTotal|O3EInt32|4|||
**1802**|**EnergyProductionPhotovoltaic**|*O3EComplexType*|80|||
| |- PhotovoltaicProductionToday|O3EInt32|4|||
| |- PhotovoltaicProductionWeek|O3EInt32|4|||
| |- PhotovoltaicProductionMonth|O3EInt32|4|||
| |- PhotovoltaicProductionYear|O3EInt32|4|||
| |- PhotovoltaicProductionTotal|O3EInt32|4|||
| |- PhotovoltaicProductionToday1|O3EInt32|4|||
| |- PhotovoltaicProductionWeek1|O3EInt32|4|||
| |- PhotovoltaicProductionMonth1|O3EInt32|4|||
| |- PhotovoltaicProductionYear1|O3EInt32|4|||
| |- PhotovoltaicProductionTotal1|O3EInt32|4|||
| |- PhotovoltaicProductionToday2|O3EInt32|4|||
| |- PhotovoltaicProductionWeek2|O3EInt32|4|||
| |- PhotovoltaicProductionMonth2|O3EInt32|4|||
| |- PhotovoltaicProductionYear2|O3EInt32|4|||
| |- PhotovoltaicProductionTotal2|O3EInt32|4|||
| |- PhotovoltaicProductionToday3|O3EInt32|4|||
| |- PhotovoltaicProductionWeek3|O3EInt32|4|||
| |- PhotovoltaicProductionMonth3|O3EInt32|4|||
| |- PhotovoltaicProductionYear3|O3EInt32|4|||
| |- PhotovoltaicProductionTotal3|O3EInt32|4|||
**1807**|**ElectricalEnergyInverterDcInputOne**|RawCodec|10|||
**1808**|**ElectricalEnergyInverterDcInputTwo**|RawCodec|10|||
**1809**|**ElectricalEnergyInverterDcInputThree**|RawCodec|10|||
**1810**|**ElectricalEnergyInverterPowerAc**|*O3EComplexType*|4|||
| |- ActivePower|O3EInt16|2|||
| |- ReactivePower|O3EInt16|2|||
**1811**|**ElectricalEnergyStorageModuleSetUpCheck**|RawCodec|1|||
**1812**|**PointOfCommonCouplingConfiguredEnergyMeter**|RawCodec|2|||
**1813**|**EnhancedVapourInjectionValve**|O3EInt8|1|||
**1814**|**ReceiverLiquidLevelSensor**|RawCodec|5|||
**1815**|**ElectricalHeaterPhaseOne**|O3EInt8|1|||
**1816**|**ElectricalHeaterPhaseTwo**|O3EInt8|1|||
**1817**|**ElectricalHeaterPhaseThree**|O3EInt8|1|||
**1819**|**SolarPumpConfigurationSelection**|O3EByteVal|1|||
**1822**|**ThreePhaseInverterCurrent**|RawCodec|51|||
**1823**|**ThreePhaseInverterVoltage**|RawCodec|27|||
**1824**|**ThreePhaseInverterCurrentPower**|*O3EComplexType*|16|||
| |- cumulated|O3EInt32|4|||
| |- L1|O3EInt32|4|||
| |- L2|O3EInt32|4|||
| |- L3|O3EInt32|4|||
**1825**|**ThreePhaseInverterCurrentApparentPower**|*O3EComplexType*|16|||
| |- cumulated|O3EInt32|4|||
| |- L1|O3EInt32|4|||
| |- L2|O3EInt32|4|||
| |- L3|O3EInt32|4|||
**1826**|**ThreePhaseInverterMaximunNominalPower**|*O3EComplexType*|4|||
| |- Power|O3EInt16|2|||
| |- Unknown|RawCodec|2|||
**1827**|**InverterElectricalEnergyStorageMaximumNominalChargePower**|*O3EComplexType*|4|||
| |- Power|O3EInt16|2|||
| |- Unknown|RawCodec|2|||
**1828**|**InverterElectricalEnergyStorageCurrentMaximumlChargePower**|*O3EComplexType*|4|||
| |- Power|O3EInt16|2|||
| |- Unknown|RawCodec|2|||
**1829**|**InverterElectricalEnergyStorageMaximumNominalDischargePower**|*O3EComplexType*|4|||
| |- Power|O3EInt16|2|||
| |- Unknown|RawCodec|2|||
**1830**|**InverterElectricalEnergyStorageCurrentMaximumlDishargePower**|*O3EComplexType*|4|||
| |- Power|O3EInt16|2|||
| |- Unknown|RawCodec|2|||
**1831**|**PhotovoltaicCurrentStringPower**|*O3EComplexType*|12|||
| |- String1|O3EInt32|4|||
| |- String2|O3EInt32|4|||
| |- String3|O3EInt32|4|||
**1832**|**PhotovoltaicStringCurrent**|*O3EComplexType*|12|||
| |- String1|O3EInt32|4|||
| |- String2|O3EInt32|4|||
| |- String3|O3EInt32|4|||
**1833**|**PhotovoltaicStringVoltage**|*O3EComplexType*|12|||
| |- String1|O3EInt32|4|||
| |- String2|O3EInt32|4|||
| |- String3|O3EInt32|4|||
**1834**|**ElectricalEnergyStorageStateOfEnergy**|*O3EComplexType*|4|||
| |- StateOfEnergy|O3EInt16|2|||
| |- Unknown|O3EInt16|2|||
**1835**|**ManufacturerProperties**|RawCodec|20|||
**1836**|**ElectricalEnergyStorageCurrentPower**|O3EInt32|4|||
**1837**|**ElectricalEnergyStorageCurrent**|*O3EComplexType*|4|||
| |- Current|O3EInt16|2|||
| |- Unknown|RawCodec|2|||
**1838**|**ElectricalEnergyStorageVoltage**|O3EInt16|2|||
**1839**|**ElectricalEnergyStorageUsableEnergy**|RawCodec|4|||
**1840**|**ElectricalEnergyStorageUsableNominalEnergy**|RawCodec|4|||
**1841**|**PointOfCommonCouplingOverview**|RawCodec|32|||
**1842**|**SecondaryCircuitFourThreeWayValve**|*O3EComplexType*|2|||
| |- Setpoint|O3EInt8|1|||
| |- CurrentPosition|O3EInt8|1|||
**1843**|**MixerOneCircuitHumidityProtection**|RawCodec|2|||
**1844**|**MixerTwoCircuitHumidityProtection**|RawCodec|2|||
**1845**|**HeatPumpCompressorEnvelope**|RawCodec|36|||
**1846**|**HeatPumpCompressorCurrentOperatingPoint**|RawCodec|4|||
**1847**|**CustomerDetailsExtensions**|RawCodec|81|||
**1848**|**ApartmentOneProperty**|RawCodec|27|||
**1849**|**ApartmentOneSetpoints**|RawCodec|50|||
**1850**|**ApartmentOneTimeScheduleMonday**|RawCodec|57|||
**1851**|**ApartmentOneTimeScheduleTuesday**|RawCodec|57|||
**1852**|**ApartmentOneTimeScheduleWednesday**|RawCodec|57|||
**1853**|**ApartmentOneTimeScheduleThursday**|RawCodec|57|||
**1854**|**ApartmentOneTimeScheduleFriday**|RawCodec|57|||
**1855**|**ApartmentOneTimeScheduleSaturday**|RawCodec|57|||
**1856**|**ApartmentOneTimeScheduleSunday**|RawCodec|57|||
**1884**|**RoomOneProperty**|RawCodec|84|||
**1884**|**RoomOneProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1885**|**RoomOneSetpoints**|RawCodec|30|||
**1886**|**RoomOneCurrentValues**|RawCodec|46|||
**1887**|**RoomTwoProperty**|RawCodec|84|||
**1887**|**RoomTwoProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1888**|**RoomTwoSetpoints**|RawCodec|30|||
**1889**|**RoomTwoCurrentValues**|RawCodec|46|||
**1890**|**RoomThreeProperty**|RawCodec|84|||
**1890**|**RoomThreeProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1891**|**RoomThreeSetpoints**|RawCodec|30|||
**1892**|**RoomThreeCurrentValues**|RawCodec|46|||
**1893**|**RoomFourProperty**|RawCodec|84|||
**1893**|**RoomFourProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1894**|**RoomFourSetpoints**|RawCodec|30|||
**1895**|**RoomFourCurrentValues**|RawCodec|46|||
**1896**|**RoomFiveProperty**|RawCodec|84|||
**1896**|**RoomFiveProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1897**|**RoomFiveSetpoints**|RawCodec|30|||
**1898**|**RoomFiveCurrentValues**|RawCodec|46|||
**1899**|**RoomSixProperty**|RawCodec|84|||
**1899**|**RoomSixProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1900**|**RoomSixSetpoints**|RawCodec|30|||
**1901**|**RoomSixCurrentValues**|RawCodec|46|||
**1902**|**RoomSevenProperty**|RawCodec|84|||
**1902**|**RoomSevenProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1903**|**RoomSevenSetpoints**|RawCodec|30|||
**1904**|**RoomSevenCurrentValues**|RawCodec|46|||
**1905**|**RoomEightProperty**|RawCodec|84|||
**1905**|**RoomEightProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1906**|**RoomEightSetpoints**|RawCodec|30|||
**1907**|**RoomEightCurrentValues**|RawCodec|46|||
**1908**|**RoomNineProperty**|RawCodec|84|||
**1908**|**RoomNineProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1909**|**RoomNineSetpoints**|RawCodec|30|||
**1910**|**RoomNineCurrentValues**|RawCodec|46|||
**1911**|**RoomTenProperty**|RawCodec|84|||
**1911**|**RoomTenProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1912**|**RoomTenSetpoints**|RawCodec|30|||
**1913**|**RoomTenCurrentValues**|RawCodec|46|||
**1914**|**RoomElevenProperty**|RawCodec|84|||
**1915**|**RoomElevenSetpoints**|RawCodec|30|||
**1916**|**RoomElevenCurrentValues**|RawCodec|46|||
**1917**|**RoomTwelveProperty**|RawCodec|84|||
**1918**|**RoomTwelveSetpoints**|RawCodec|30|||
**1919**|**RoomTwelveCurrentValues**|RawCodec|46|||
**1920**|**RoomThirteenProperty**|RawCodec|84|||
**1920**|**RoomThirteenProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1921**|**RoomThirteenSetpoints**|RawCodec|30|||
**1922**|**RoomThirteenCurrentValues**|RawCodec|46|||
**1923**|**RoomFourteenProperty**|RawCodec|84|||
**1923**|**RoomFourteenProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1924**|**RoomFourteenSetpoints**|RawCodec|30|||
**1925**|**RoomFourteenCurrentValues**|RawCodec|46|||
**1926**|**RoomFifteenProperty**|RawCodec|84|||
**1926**|**RoomFifteenProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1927**|**RoomFifteenSetpoints**|RawCodec|30|||
**1928**|**RoomFifteenCurrentValues**|RawCodec|46|||
**1929**|**RoomSixteenProperty**|RawCodec|84|||
**1929**|**RoomSixteenProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1930**|**RoomSixteenSetpoints**|RawCodec|30|||
**1931**|**RoomSixteenCurrentValues**|RawCodec|46|||
**1932**|**RoomSeventeenProperty**|RawCodec|84|||
**1932**|**RoomSeventeenProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1933**|**RoomSeventeenSetpoints**|RawCodec|30|||
**1934**|**RoomSeventeenCurrentValues**|RawCodec|46|||
**1935**|**RoomEighteenProperty**|RawCodec|84|||
**1935**|**RoomEightteenProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1936**|**RoomEighteenSetpoints**|RawCodec|30|||
**1937**|**RoomEighteenCurrentValues**|RawCodec|46|||
**1938**|**RoomNineteenProperty**|RawCodec|84|||
**1938**|**RoomNineteenProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1939**|**RoomNineteenSetpoints**|RawCodec|30|||
**1940**|**RoomNineteenCurrentValues**|RawCodec|46|||
**1941**|**RoomTwentyProperty**|RawCodec|84|||
**1941**|**RoomTwentyProperty**|*O3EComplexType*|85|||
| |- Roomname|O3EUtf8|39|||
| |- Unknown1|RawCodec|4|||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1|||
| |- Unknown2|RawCodec|1|||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1|||
| |- Unknown3|RawCodec|29|||
| |- WindowDetection|O3EEnum|1|||
| |- Unknown4|RawCodec|9|||
**1942**|**RoomTwentySetpoints**|RawCodec|30|||
**1943**|**RoomTwentyCurrentValues**|RawCodec|46|||
**1944**|**RoomOneTimeScheduleMonday**|RawCodec|57|||
**1945**|**RoomOneTimeScheduleTuesday**|RawCodec|57|||
**1946**|**RoomOneTimeScheduleWednesday**|RawCodec|57|||
**1947**|**RoomOneTimeScheduleThursday**|RawCodec|57|||
**1948**|**RoomOneTimeScheduleFriday**|RawCodec|57|||
**1949**|**RoomOneTimeScheduleSaturday**|RawCodec|57|||
**1950**|**RoomOneTimeScheduleSunday**|RawCodec|57|||
**1951**|**RoomTwoTimeScheduleMonday**|RawCodec|57|||
**1952**|**RoomTwoTimeScheduleTuesday**|RawCodec|57|||
**1953**|**RoomTwoTimeScheduleWednesday**|RawCodec|57|||
**1954**|**RoomTwoTimeScheduleThursday**|RawCodec|57|||
**1955**|**RoomTwoTimeScheduleFriday**|RawCodec|57|||
**1956**|**RoomTwoTimeScheduleSaturday**|RawCodec|57|||
**1957**|**RoomTwoTimeScheduleSunday**|RawCodec|57|||
**1958**|**RoomThreeTimeScheduleMonday**|RawCodec|57|||
**1959**|**RoomThreeTimeScheduleTuesday**|RawCodec|57|||
**1960**|**RoomThreeTimeScheduleWednesday**|RawCodec|57|||
**1961**|**RoomThreeTimeScheduleThursday**|RawCodec|57|||
**1962**|**RoomThreeTimeScheduleFriday**|RawCodec|57|||
**1963**|**RoomThreeTimeScheduleSaturday**|RawCodec|57|||
**1964**|**RoomThreeTimeScheduleSunday**|RawCodec|57|||
**1965**|**RoomFourTimeScheduleMonday**|RawCodec|57|||
**1966**|**RoomFourTimeScheduleTuesday**|RawCodec|57|||
**1967**|**RoomFourTimeScheduleWednesday**|RawCodec|57|||
**1968**|**RoomFourTimeScheduleThursday**|RawCodec|57|||
**1969**|**RoomFourTimeScheduleFriday**|RawCodec|57|||
**1970**|**RoomFourTimeScheduleSaturday**|RawCodec|57|||
**1971**|**RoomFourTimeScheduleSunday**|RawCodec|57|||
**1972**|**RoomFiveTimeScheduleMonday**|RawCodec|57|||
**1973**|**RoomFiveTimeScheduleTuesday**|RawCodec|57|||
**1974**|**RoomFiveTimeScheduleWednesday**|RawCodec|57|||
**1975**|**RoomFiveTimeScheduleThursday**|RawCodec|57|||
**1976**|**RoomFiveTimeScheduleFriday**|RawCodec|57|||
**1977**|**RoomFiveTimeScheduleSaturday**|RawCodec|57|||
**1978**|**RoomFiveTimeScheduleSunday**|RawCodec|57|||
**1979**|**RoomSixTimeScheduleMonday**|RawCodec|57|||
**1980**|**RoomSixTimeScheduleTuesday**|RawCodec|57|||
**1981**|**RoomSixTimeScheduleWednesday**|RawCodec|57|||
**1982**|**RoomSixTimeScheduleThursday**|RawCodec|57|||
**1983**|**RoomSixTimeScheduleFriday**|RawCodec|57|||
**1984**|**RoomSixTimeScheduleSaturday**|RawCodec|57|||
**1985**|**RoomSixTimeScheduleSunday**|RawCodec|57|||
**1986**|**RoomSevenTimeScheduleMonday**|RawCodec|57|||
**1987**|**RoomSevenTimeScheduleTuesday**|RawCodec|57|||
**1988**|**RoomSevenTimeScheduleWednesday**|RawCodec|57|||
**1989**|**RoomSevenTimeScheduleThursday**|RawCodec|57|||
**1990**|**RoomSevenTimeScheduleFriday**|RawCodec|57|||
**1991**|**RoomSevenTimeScheduleSaturday**|RawCodec|57|||
**1992**|**RoomSevenTimeScheduleSunday**|RawCodec|57|||
**1993**|**RoomEightTimeScheduleMonday**|RawCodec|57|||
**1994**|**RoomEightTimeScheduleTuesday**|RawCodec|57|||
**1995**|**RoomEightTimeScheduleWednesday**|RawCodec|57|||
**1996**|**RoomEightTimeScheduleThursday**|RawCodec|57|||
**1997**|**RoomEightTimeScheduleFriday**|RawCodec|57|||
**1998**|**RoomEightTimeScheduleSaturday**|RawCodec|57|||
**1999**|**RoomEightTimeScheduleSunday**|RawCodec|57|||
**2000**|**RoomNineTimeScheduleMonday**|RawCodec|57|||
**2001**|**RoomNineTimeScheduleTuesday**|RawCodec|57|||
**2002**|**RoomNineTimeScheduleWednesday**|RawCodec|57|||
**2003**|**RoomNineTimeScheduleThursday**|RawCodec|57|||
**2004**|**RoomNineTimeScheduleFriday**|RawCodec|57|||
**2005**|**RoomNineTimeScheduleSaturday**|RawCodec|57|||
**2006**|**RoomNineTimeScheduleSunday**|RawCodec|57|||
**2007**|**RoomTenTimeScheduleMonday**|RawCodec|57|||
**2008**|**RoomTenTimeScheduleTuesday**|RawCodec|57|||
**2009**|**RoomTenTimeScheduleWednesday**|RawCodec|57|||
**2010**|**RoomTenTimeScheduleThursday**|RawCodec|57|||
**2011**|**RoomTenTimeScheduleFriday**|RawCodec|57|||
**2012**|**RoomTenTimeScheduleSaturday**|RawCodec|57|||
**2013**|**RoomTenTimeScheduleSunday**|RawCodec|57|||
**2014**|**RoomElevenTimeScheduleMonday**|RawCodec|57|||
**2015**|**RoomElevenTimeScheduleTuesday**|RawCodec|57|||
**2016**|**RoomElevenTimeScheduleWednesday**|RawCodec|57|||
**2017**|**RoomElevenTimeScheduleThursday**|RawCodec|57|||
**2018**|**RoomElevenTimeScheduleFriday**|RawCodec|57|||
**2019**|**RoomElevenTimeScheduleSaturday**|RawCodec|57|||
**2020**|**RoomElevenTimeScheduleSunday**|RawCodec|57|||
**2021**|**RoomTwelveTimeScheduleMonday**|RawCodec|57|||
**2022**|**RoomTwelveTimeScheduleTuesday**|RawCodec|57|||
**2023**|**RoomTwelveTimeScheduleWednesday**|RawCodec|57|||
**2024**|**RoomTwelveTimeScheduleThursday**|RawCodec|57|||
**2025**|**RoomTwelveTimeScheduleFriday**|RawCodec|57|||
**2026**|**RoomTwelveTimeScheduleSaturday**|RawCodec|57|||
**2027**|**RoomTwelveTimeScheduleSunday**|RawCodec|57|||
**2028**|**RoomThirteenTimeScheduleMonday**|RawCodec|57|||
**2029**|**RoomThirteenTimeScheduleTuesday**|RawCodec|57|||
**2030**|**RoomThirteenTimeScheduleWednesday**|RawCodec|57|||
**2031**|**RoomThirteenTimeScheduleThursday**|RawCodec|57|||
**2032**|**RoomThirteenTimeScheduleFriday**|RawCodec|57|||
**2033**|**RoomThirteenTimeScheduleSaturday**|RawCodec|57|||
**2034**|**RoomThirteenTimeScheduleSunday**|RawCodec|57|||
**2035**|**RoomFourteenTimeScheduleMonday**|RawCodec|57|||
**2036**|**RoomFourteenTimeScheduleTuesday**|RawCodec|57|||
**2037**|**RoomFourteenTimeScheduleWednesday**|RawCodec|57|||
**2038**|**RoomFourteenTimeScheduleThursday**|RawCodec|57|||
**2039**|**RoomFourteenTimeScheduleFriday**|RawCodec|57|||
**2040**|**RoomFourteenTimeScheduleSaturday**|RawCodec|57|||
**2041**|**RoomFourteenTimeScheduleSunday**|RawCodec|57|||
**2042**|**RoomFifteenTimeScheduleMonday**|RawCodec|57|||
**2043**|**RoomFifteenTimeScheduleTuesday**|RawCodec|57|||
**2044**|**RoomFifteenTimeScheduleWednesday**|RawCodec|57|||
**2045**|**RoomFifteenTimeScheduleThursday**|RawCodec|57|||
**2046**|**RoomFifteenTimeScheduleFriday**|RawCodec|57|||
**2047**|**RoomFifteenTimeScheduleSaturday**|RawCodec|57|||
**2048**|**RoomFifteenTimeScheduleSunday**|RawCodec|57|||
**2049**|**RoomSixteenTimeScheduleMonday**|RawCodec|57|||
**2050**|**RoomSixteenTimeScheduleTuesday**|RawCodec|57|||
**2051**|**RoomSixteenTimeScheduleWednesday**|RawCodec|57|||
**2052**|**RoomSixteenTimeScheduleThursday**|RawCodec|57|||
**2053**|**RoomSixteenTimeScheduleFriday**|RawCodec|57|||
**2054**|**RoomSixteenTimeScheduleSaturday**|RawCodec|57|||
**2055**|**RoomSixteenTimeScheduleSunday**|RawCodec|57|||
**2056**|**RoomSeventeenTimeScheduleMonday**|RawCodec|57|||
**2057**|**RoomSeventeenTimeScheduleTuesday**|RawCodec|57|||
**2058**|**RoomSeventeenTimeScheduleWednesday**|RawCodec|57|||
**2059**|**RoomSeventeenTimeScheduleThursday**|RawCodec|57|||
**2060**|**RoomSeventeenTimeScheduleFriday**|RawCodec|57|||
**2061**|**RoomSeventeenTimeScheduleSaturday**|RawCodec|57|||
**2062**|**RoomSeventeenTimeScheduleSunday**|RawCodec|57|||
**2063**|**RoomEighteenTimeScheduleMonday**|RawCodec|57|||
**2064**|**RoomEighteenTimeScheduleTuesday**|RawCodec|57|||
**2065**|**RoomEighteenTimeScheduleWednesday**|RawCodec|57|||
**2066**|**RoomEighteenTimeScheduleThursday**|RawCodec|57|||
**2067**|**RoomEighteenTimeScheduleFriday**|RawCodec|57|||
**2068**|**RoomEighteenTimeScheduleSaturday**|RawCodec|57|||
**2069**|**RoomEighteenTimeScheduleSunday**|RawCodec|57|||
**2070**|**RoomNineteenTimeScheduleMonday**|RawCodec|57|||
**2071**|**RoomNineteenTimeScheduleTuesday**|RawCodec|57|||
**2072**|**RoomNineteenTimeScheduleWednesday**|RawCodec|57|||
**2073**|**RoomNineteenTimeScheduleThursday**|RawCodec|57|||
**2074**|**RoomNineteenTimeScheduleFriday**|RawCodec|57|||
**2075**|**RoomNineteenTimeScheduleSaturday**|RawCodec|57|||
**2076**|**RoomNineteenTimeScheduleSunday**|RawCodec|57|||
**2077**|**RoomTwentyTimeScheduleMonday**|RawCodec|57|||
**2078**|**RoomTwentyTimeScheduleTuesday**|RawCodec|57|||
**2079**|**RoomTwentyTimeScheduleWednesday**|RawCodec|57|||
**2080**|**RoomTwentyTimeScheduleThursday**|RawCodec|57|||
**2081**|**RoomTwentyTimeScheduleFriday**|RawCodec|57|||
**2082**|**RoomTwentyTimeScheduleSaturday**|RawCodec|57|||
**2083**|**RoomTwentyTimeScheduleSunday**|RawCodec|57|||
**2084**|**ZigBeeOneDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2085**|**ZigBeeOneDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2086**|**ZigBeeOneDeviceCurrentValues**|RawCodec|57|||
**2086**|**ZigBeeOneDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- ValveType|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2087**|**ZigBeeTwoDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2088**|**ZigBeeTwoDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2089**|**ZigBeeTwoDeviceCurrentValues**|RawCodec|57|||
**2089**|**ZigBeeTwoDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2090**|**ZigBeeThreeDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2091**|**ZigBeeThreeDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2092**|**ZigBeeThreeDeviceCurrentValues**|RawCodec|57|||
**2092**|**ZigBeeThreeDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2093**|**ZigBeeFourDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2094**|**ZigBeeFourDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2095**|**ZigBeeFourDeviceCurrentValues**|RawCodec|57|||
**2095**|**ZigBeeFourDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2096**|**ZigBeeFiveDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2097**|**ZigBeeFiveDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2098**|**ZigBeeFiveDeviceCurrentValues**|RawCodec|57|||
**2098**|**ZigBeeFiveDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2099**|**ZigBeeSixDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2100**|**ZigBeeSixDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2101**|**ZigBeeSixDeviceCurrentValues**|RawCodec|57|||
**2101**|**ZigBeeSixDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2102**|**ZigBeeSevenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2103**|**ZigBeeSevenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2104**|**ZigBeeSevenDeviceCurrentValues**|RawCodec|57|||
**2104**|**ZigBeeSevenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2105**|**ZigBeeEightDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2106**|**ZigBeeEightDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2107**|**ZigBeeEightDeviceCurrentValues**|RawCodec|57|||
**2107**|**ZigBeeEightDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2108**|**ZigBeeNineDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2109**|**ZigBeeNineDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2110**|**ZigBeeNineDeviceCurrentValues**|RawCodec|57|||
**2110**|**ZigBeeNineDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2111**|**ZigBeeTenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2112**|**ZigBeeTenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2113**|**ZigBeeTenDeviceCurrentValues**|RawCodec|57|||
**2113**|**ZigBeeTenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2114**|**ZigBeeElevenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2115**|**ZigBeeElevenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2116**|**ZigBeeElevenDeviceCurrentValues**|RawCodec|57|||
**2116**|**ZigBeeElevenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2117**|**ZigBeeTwelveDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2118**|**ZigBeeTwelveDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2119**|**ZigBeeTwelveDeviceCurrentValues**|RawCodec|57|||
**2119**|**ZigBeeTwelveDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2120**|**ZigBeeThirteenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2121**|**ZigBeeThirteenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2122**|**ZigBeeThirteenDeviceCurrentValues**|RawCodec|57|||
**2122**|**ZigBeeThirteenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2123**|**ZigBeeFourteenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2124**|**ZigBeeFourteenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2125**|**ZigBeeFourteenDeviceCurrentValues**|RawCodec|57|||
**2125**|**ZigBeeFourteenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2126**|**ZigBeeFifteenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2127**|**ZigBeeFifteenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2128**|**ZigBeeFifteenDeviceCurrentValues**|RawCodec|57|||
**2128**|**ZigBeeFifteenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2129**|**ZigBeeSixteenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2130**|**ZigBeeSixteenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2131**|**ZigBeeSixteenDeviceCurrentValues**|RawCodec|57|||
**2131**|**ZigBeeSixteenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2132**|**ZigBeeSeventeenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2133**|**ZigBeeSeventeenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2134**|**ZigBeeSeventeenDeviceCurrentValues**|RawCodec|57|||
**2134**|**ZigBeeSeventeenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2135**|**ZigBeeEighteenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2136**|**ZigBeeEighteenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2137**|**ZigBeeEighteenDeviceCurrentValues**|RawCodec|57|||
**2137**|**ZigBeeEighteenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2138**|**ZigBeeNineteenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2139**|**ZigBeeNineteenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2140**|**ZigBeeNineteenDeviceCurrentValues**|RawCodec|57|||
**2140**|**ZigBeeNineteenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2141**|**ZigBeeTwentyDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2142**|**ZigBeeTwentyDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2143**|**ZigBeeTwentyDeviceCurrentValues**|RawCodec|57|||
**2143**|**ZigBeeTwentyDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2144**|**PointOfCommonCouplingAcActiveCurrent**|RawCodec|16|||
**2145**|**ObjectTopology**|RawCodec|38|||
**2146**|**ZigBeeApartmentOneProperty**|RawCodec|8|||
**2147**|**ZigBeeApartmentOneTopology**|RawCodec|106|||
**2158**|**ActivatedFeatures**|RawCodec|16|||
**2159**|**ApartmentOneCurrentValues**|RawCodec|84|||
**2164**|**DeviceDigitalInputSixValue**|O3EByteVal|1|||
**2165**|**DevicePwmOutputThreeValue**|O3EInt8|1|||
**2166**|**MixerOneCircuitExternalHookupDemandInput**|RawCodec|1|||
**2167**|**MixerTwoCircuitExternalHookupDemandInput**|RawCodec|1|||
**2168**|**MixerThreeCircuitExternalHookupDemandInput**|RawCodec|1|||
**2169**|**MixerFourCircuitExternalHookupDemandInput**|RawCodec|1|||
**2182**|**SupportedApartmentFeatures**|RawCodec|15|||
**2183**|**ActivatedApartmentFeatures**|RawCodec|15|||
**2184**|**BackupBoxTest**|RawCodec|2|||
**2185**|**BatteryStateOfChargeHistogram**|RawCodec|40|||
**2188**|**PointOfCommonCouplingSetActivePowerTotal**|RawCodec|6|||
**2189**|**EebusDeviceListTwo**|RawCodec|104|||
**2190**|**EebusDeviceListThree**|RawCodec|104|||
**2191**|**EebusDeviceListFour**|RawCodec|104|||
**2192**|**EebusDeviceListFive**|RawCodec|104|||
**2193**|**ApartmentOneSupplyChannelTwoTimeScheduleMonday**|RawCodec|57|||
**2194**|**ApartmentOneSupplyChannelTwoTimeScheduleTuesday**|RawCodec|57|||
**2195**|**ApartmentOneSupplyChannelTwoTimeScheduleWednesday**|RawCodec|57|||
**2196**|**ApartmentOneSupplyChannelTwoTimeScheduleThursday**|RawCodec|57|||
**2197**|**ApartmentOneSupplyChannelTwoTimeScheduleFriday**|RawCodec|57|||
**2198**|**ApartmentOneSupplyChannelTwoTimeScheduleSaturday**|RawCodec|57|||
**2199**|**ApartmentOneSupplyChannelTwoTimeScheduleSunday**|RawCodec|57|||
**2200**|**ApartmentOneSupplyChannelThreeTimeScheduleMonday**|RawCodec|57|||
**2201**|**ApartmentOneSupplyChannelThreeTimeScheduleTuesday**|RawCodec|57|||
**2202**|**ApartmentOneSupplyChannelThreeTimeScheduleWednesday**|RawCodec|57|||
**2203**|**ApartmentOneSupplyChannelThreeTimeScheduleThursday**|RawCodec|57|||
**2204**|**ApartmentOneSupplyChannelThreeTimeScheduleFriday**|RawCodec|57|||
**2205**|**ApartmentOneSupplyChannelThreeTimeScheduleSaturday**|RawCodec|57|||
**2206**|**ApartmentOneSupplyChannelThreeTimeScheduleSunday**|RawCodec|57|||
**2207**|**ApartmentOneSupplyChannelFourTimeScheduleMonday**|RawCodec|57|||
**2208**|**ApartmentOneSupplyChannelFourTimeScheduleTuesday**|RawCodec|57|||
**2209**|**ApartmentOneSupplyChannelFourTimeScheduleWednesday**|RawCodec|57|||
**2210**|**ApartmentOneSupplyChannelFourTimeScheduleThursday**|RawCodec|57|||
**2211**|**ApartmentOneSupplyChannelFourTimeScheduleFriday**|RawCodec|57|||
**2212**|**ApartmentOneSupplyChannelFourTimeScheduleSaturday**|RawCodec|57|||
**2213**|**ApartmentOneSupplyChannelFourTimeScheduleSunday**|RawCodec|57|||
**2214**|**BackupBoxConfiguration**|*O3EComplexType*|2|||
| |- DischargeLimit|O3EInt8|1|||
| |- Unknown|O3EInt8|1|||
**2217**|**InputDemandSideManagementlReceiver**|RawCodec|1|||
**2218**|**RemoteLimitValueDemandSideManagement**|RawCodec|4|||
**2219**|**BatteryCalibration**|RawCodec|1|||
**2220**|**BatteryReactivePowerMode**|RawCodec|1|||
**2221**|**BatteryReactivePowerFixCosinusPhi**|RawCodec|3|||
**2222**|**BatteryReactivePower**|RawCodec|18|||
**2223**|**BatteryReactivePowerCosinusPhi**|RawCodec|15|||
**2224**|**PhotovoltaicsActivePowerLimitation**|RawCodec|16|||
**2225**|**ElectricEnergyStorageSetpoint**|RawCodec|12|||
**2226**|**ElectricEnergyStorageMaximum**|RawCodec|12|||
**2229**|**ThermostatTerminalOneFunction**|RawCodec|1|||
**2230**|**ThermostatTerminalTwoFunction**|RawCodec|1|||
**2231**|**ThermostatTerminalThreeFunction**|RawCodec|1|||
**2233**|**PersistentStorageStatus**|O3EByteVal|1|||
**2234**|**PowerGridCodeSettingsNormOne**|RawCodec|27|||
**2235**|**CascadeSystemConfiguration**|RawCodec|65|||
**2236**|**CascadeDeviceSetpoint**|RawCodec|10|||
**2237**|**CascadeDeviceStatus**|RawCodec|18|||
**2239**|**ElectricEnergyStorageControlMode**|RawCodec|1|||
**2240**|**BatteryTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**2241**|**OutsideTemperatureSensorSource**|RawCodec|1|||
**2242**|**PowerGridCodeSettingsNormTwo**|RawCodec|27|||
**2244**|**PowerGridCodeSettingsNormFour**|RawCodec|27|||
**2246**|**FixReactivePowerIn**|RawCodec|26|||
**2247**|**FilterRuntime**|*O3EComplexType*|12|||
| |- Actual|O3EInt32|4|||
| |- Remaining|O3EInt32|4|||
| |- Overdue|O3EInt32|4|||
**2248**|**CurrentVentilationHeatRecovery**|O3EByteVal|1|||
**2249**|**DigitalSwitchSettingOne**|RawCodec|8|||
**2250**|**DigitalSwitchSettingTwo**|RawCodec|8|||
**2251**|**LedStatusOne**|RawCodec|8|||
**2252**|**LedStatusTwo**|RawCodec|8|||
**2253**|**DeviceDigitalInputSevenValue**|O3EByteVal|1|||
**2254**|**PowerGridCodeSettingConfiguration**|RawCodec|1|||
**2255**|**MinimumSecondaryReturnTemperatureRefrigerantCircuit**|O3EInt16|2|||
**2256**|**DesiredThermalEnergyDefrost**|O3EInt16|2|||
**2257**|**DomesticHotWaterTemperatureSetpointOffset**|O3EInt16|2|||
**2259**|**RefrigerationCircuitStatus**|O3EByteVal|1|||
**2260**|**ZigBeeTwentyOneDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2261**|**ZigBeeTwentyOneDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2262**|**ZigBeeTwentyOneDeviceCurrentValues**|RawCodec|57|||
**2262**|**ZigBeeTwentyOneDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2263**|**ZigBeeTwentyTwoDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2264**|**ZigBeeTwentyTwoDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2265**|**ZigBeeTwentyTwoDeviceCurrentValues**|RawCodec|57|||
**2265**|**ZigBeeTwentyTwoDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2266**|**ZigBeeTwentyThreeDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2267**|**ZigBeeTwentyThreeDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2268**|**ZigBeeTwentyThreeDeviceCurrentValues**|RawCodec|57|||
**2268**|**ZigBeeTwentyThreeDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2269**|**ZigBeeTwentyFourDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2270**|**ZigBeeTwentyFourDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2271**|**ZigBeeTwentyFourDeviceCurrentValues**|RawCodec|57|||
**2271**|**ZigBeeTwentyFourDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2272**|**ZigBeeTwentyFiveDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2273**|**ZigBeeTwentyFiveDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2274**|**ZigBeeTwentyFiveDeviceCurrentValues**|RawCodec|57|||
**2274**|**ZigBeeTwentyFiveDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2275**|**ZigBeeTwentySixDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2276**|**ZigBeeTwentySixDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2277**|**ZigBeeTwentySixDeviceCurrentValues**|RawCodec|57|||
**2277**|**ZigBeeTwentySixDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2278**|**ZigBeeTwentySevenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2279**|**ZigBeeTwentySevenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2280**|**ZigBeeTwentySevenDeviceCurrentValues**|RawCodec|57|||
**2280**|**ZigBeeTwentySevenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2281**|**ZigBeeTwentyEightDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2282**|**ZigBeeTwentyEightDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2283**|**ZigBeeTwentyEightDeviceCurrentValues**|RawCodec|57|||
**2283**|**ZigBeeTwentyEightDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2284**|**ZigBeeTwentyNineDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2285**|**ZigBeeTwentyNineDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2286**|**ZigBeeTwentyNineDeviceCurrentValues**|RawCodec|57|||
**2286**|**ZigBeeTwentyNineDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2287**|**ZigBeeThirtyDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2288**|**ZigBeeThirtyDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2289**|**ZigBeeThirtyDeviceCurrentValues**|RawCodec|57|||
**2289**|**ZigBeeThirtyDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2290**|**ZigBeeThirtyOneDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2291**|**ZigBeeThirtyOneDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2292**|**ZigBeeThirtyOneDeviceCurrentValues**|RawCodec|57|||
**2292**|**ZigBeeThirtyOneDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2293**|**ZigBeeThirtyTwoDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2294**|**ZigBeeThirtyTwoDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2295**|**ZigBeeThirtyTwoDeviceCurrentValues**|RawCodec|57|||
**2295**|**ZigBeeThirtyTwoDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2296**|**ZigBeeThirtyThreeDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2297**|**ZigBeeThirtyThreeDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2298**|**ZigBeeThirtyThreeDeviceCurrentValues**|RawCodec|57|||
**2298**|**ZigBeeThirtyThreeDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2299**|**ZigBeeThirtyFourDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2300**|**ZigBeeThirtyFourDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2301**|**ZigBeeThirtyFourDeviceCurrentValues**|RawCodec|57|||
**2301**|**ZigBeeThirtyFourDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2302**|**ZigBeeThirtyFiveDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2303**|**ZigBeeThirtyFiveDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2304**|**ZigBeeThirtyFiveDeviceCurrentValues**|RawCodec|57|||
**2304**|**ZigBeeThirtyFiveDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2305**|**ZigBeeThirtySixDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2306**|**ZigBeeThirtySixDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2307**|**ZigBeeThirtySixDeviceCurrentValues**|RawCodec|57|||
**2307**|**ZigBeeThirtySixDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2308**|**ZigBeeThirtySevenDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2309**|**ZigBeeThirtySevenDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2310**|**ZigBeeThirtySevenDeviceCurrentValues**|RawCodec|57|||
**2310**|**ZigBeeThirtySevenDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2311**|**ZigBeeThirtyEightDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2312**|**ZigBeeThirtyEightDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2313**|**ZigBeeThirtyEightDeviceCurrentValues**|RawCodec|57|||
**2313**|**ZigBeeThirtyEightDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2314**|**ZigBeeThirtyNineDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2315**|**ZigBeeThirtyNineDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2316**|**ZigBeeThirtyNineDeviceCurrentValues**|RawCodec|57|||
**2316**|**ZigBeeThirtyNineDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2317**|**ZigBeeFourtyDeviceProperty**|*O3EComplexType*|84|||
| |- Serialnumber|RawCodec|8|||
| |- SerialnumberPostfix|RawCodec|1|||
| |- Devicename|O3EUtf8|39|||
| |- Unknown1|RawCodec|1|||
| |- ViCareDevice|O3EEnum|1|||
| |- Firmware-Version|O3ESoftVers|8|||
| |- Unknown2|RawCodec|26|||
**2318**|**ZigBeeFourtyDeviceSetpoint**|*O3EComplexType*|13|||
| |- Prefix|RawCodec|2|||
| |- MaximumFlowTemperature|O3EInt16|2|||
| |- Unused|RawCodec|9|||
**2319**|**ZigBeeFourtyDeviceCurrentValues**|RawCodec|57|||
**2319**|**ZigBeeFourtyDeviceCurrentValues**|*O3EComplexType*|68|||
| |- Unknown1|RawCodec|2|||
| |- BatteryLevel|O3EInt8|1|||
| |- Unknown2|RawCodec|38|||
| |- Valve Type|O3EInt8|1|||
| |- ActualTemperature|O3EInt8|1|||
| |- OperatingStatus|O3EInt8|1|||
| |- Unknown3|RawCodec|4|||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1|||
| |- Unknown4|RawCodec|5|||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1|||
| |- DeviceTemperatureSetpoint|O3EInt8|1|||
| |- Unknown5|RawCodec|12|||
**2320**|**DomesticHotWaterStatus**|O3EByteVal|1|||
**2321**|**ZigBeeApartmentOneDecoupleList**|RawCodec|91|||
**2327**|**VentilationTargetVolumeFlow**|*O3EComplexType*|4|||
| |- ActualFlow|O3EInt16|2|||
| |- Unknown|O3EInt16|2|||
**2328**|**VentilationCurrentVolumeFlow**|*O3EComplexType*|4|||
| |- TargetFlow|O3EInt16|2|||
| |- Unknown|O3EInt16|2|||
**2329**|**BatteryEnergyUsedAverage**|RawCodec|14|||
**2330**|[**GenericDigitalInputConfigurationOnBoardTwo**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1|||
**2331**|[**GenericDigitalInputConfigurationOnBoardThree**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1|||
**2332**|[**GenericDigitalInputConfigurationOnBoardFour**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1|||
**2333**|**EconomizerLiquidTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**2334**|**EvaporatorVaporTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**2335**|**BatteryModuleCoulombCounters**|RawCodec|8|||
**2336**|**ControllerBoardTemperatureSensor**|*O3EComplexType*|9|||
| |- Sensor1|O3EInt16|2|||
| |- Sensor2|O3EInt16|2|||
| |- Unknown|RawCodec|5|||
**2337**|**UltraLowNitroOxideStatusActive**|RawCodec|1|||
**2338**|**HighLimitTestMode**|RawCodec|3|||
**2339**|**SafetyLimiterThresholdTemperature**|RawCodec|2|||
**2340**|**ElectricalHeaterConfiguration**|RawCodec|2|||
**2341**|**CoefficientOfPerformanceConfiguration**|RawCodec|4|||
**2342**|**NominalThermalCapacityHeating**|O3EInt32|4|||
**2343**|**NominalThermalCapacityCooling**|O3EInt32|4|||
**2344**|**CombustionAirInterlockSettings**|RawCodec|1|||
**2345**|**CompressorSetpointPercent**|O3EInt8|1|||
**2346**|**CompressorSpeedPercent**|O3EInt8|1|||
**2348**|**PhotovoltaicsActivePowerLimitationEnergyManagementSystem**|RawCodec|8|||
**2349**|**PhotovoltaicsActivePowerLimitationFallbackEnergyManagementSystem**|RawCodec|8|||
**2350**|**EnergyManagmentSystemResultingControlState**|O3EByteVal|1|||
**2351**|**HeatPumpCompressor**|*O3EComplexType*|2|||
| |- PowerState|O3EByteVal|1|||
| |- ErrorState|O3EByteVal|1|||
**2352**|**AdditionalElectricHeater**|*O3EComplexType*|2|||
| |- PowerState|O3EByteVal|1|||
| |- ErrorState|O3EByteVal|1|||
**2353**|**TargetDemandHeatProducer**|*O3EComplexType*|4|||
| |- StateHeating|O3EByteVal|1|||
| |- FlowTemperature|O3EInt16|2|||
| |- Modulation|O3EByteVal|1|||
**2355**|**MinimumVentilationSupplyAirTemperature**|*O3EComplexType*|4|||
| |- Sensor1|O3EInt16|2|||
| |- Sensor2|O3EInt16|2|||
**2356**|**CurrentSystemHeatingCoolingLevel**|O3EInt8|1|||
**2369**|**HeatPumpCompressorStatistical**|*O3EComplexType*|14|||
| |- Unknown1|RawCodec|6|||
| |- starts|O3EInt16|2|||
| |- Unknown2|RawCodec|2|||
| |- hours|O3EInt16|2|||
| |- Unknown3|RawCodec|2|||
**2370**|**AdditionalElectricHeaterStatistical**|*O3EComplexType*|11|||
| |- Unknown1|RawCodec|3|||
| |- starts|O3EInt16|2|||
| |- Unknown2|RawCodec|2|||
| |- hours|O3EInt16|2|||
| |- Unknown3|RawCodec|2|||
**2371**|**VentilationControlMode**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- Unknown|RawCodec|1|||
**2372**|**VentilationControllerOperationState**|*O3EComplexType*|2|||
| |- Unknown1|RawCodec|1|||
| |- Unknown2|RawCodec|1|||
**2373**|**VentilationAirVolumeFlowBalancingOffset**|RawCodec|2|||
**2374**|**VentilationExternalLockFunctionSetting**|O3EByteVal|1|||
**2375**|**NarrowBandInternetOfThingsConfiguration**|RawCodec|7|||
**2376**|**NarrowBandInternetOfThingsRadio**|RawCodec|132|||
**2377**|**EvolvedUniversalTerrestrialRadioAccessDataLinkInfo**|RawCodec|45|||
**2378**|**EvolvedUniversalTerrestrialRadioAccessNeighborCells**|RawCodec|48|||
**2379**|**EvolvedUniversalTerrestrialRadioAccessServingCellInfo**|RawCodec|22|||
**2380**|**EvolvedUniversalTerrestrialRadioAccessServingCellMeasurements**|RawCodec|17|||
**2382**|**PaddleSwitch**|RawCodec|2|||
**2403**|**BypassOperationLevel**|O3EInt8|1|||
**2404**|**BivalenceControlMode**|*O3EComplexType*|6|||
| |- OperationMode|O3EByteVal|1|||
| |- BivalenceControlTemperature|O3EInt16|2|||
| |- BivalenceControlAlternativeTemperature|O3EInt16|2|||
| |- ControlMode|O3EByteVal|1|||
**2405**|**MixerOneCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6|||
| |- EffectiveSetTemperature|O3EInt16|2|||
| |- FactorySelectedUnderfloorHeating|O3EInt16|2|||
| |- FactorySelectedFanConvector|O3EInt16|2|||
**2406**|**MixerTwoCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6|||
| |- EffectiveSetTemperature|O3EInt16|2|||
| |- FactorySelectedUnderfloorHeating|O3EInt16|2|||
| |- FactorySelectedFanConvector|O3EInt16|2|||
**2407**|**MixerThreeCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6|||
| |- EffectiveSetTemperature|O3EInt16|2|||
| |- FactorySelectedUnderfloorHeating|O3EInt16|2|||
| |- FactorySelectedFanConvector|O3EInt16|2|||
**2408**|**MixerFourCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6|||
| |- EffectiveSetTemperature|O3EInt16|2|||
| |- FactorySelectedUnderfloorHeating|O3EInt16|2|||
| |- FactorySelectedFanConvector|O3EInt16|2|||
**2409**|**MixerOneCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12|||
**2410**|**MixerTwoCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12|||
**2411**|**MixerThreeCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12|||
**2412**|**MixerFourCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12|||
**2413**|**MixerOneCircuitThresholdCooling**|*O3EComplexType*|4|||
| |- HysteresisOn|O3EInt16|2|||
| |- HysteresisOff|O3EInt16|2|||
**2414**|**MixerTwoCircuitThresholdCooling**|*O3EComplexType*|4|||
| |- HysteresisOn|O3EInt16|2|||
| |- HysteresisOff|O3EInt16|2|||
**2415**|**MixerThreeCircuitThresholdCooling**|*O3EComplexType*|4|||
| |- HysteresisOn|O3EInt16|2|||
| |- HysteresisOff|O3EInt16|2|||
**2416**|**MixerFourCircuitThresholdCooling**|*O3EComplexType*|4|||
| |- HysteresisOn|O3EInt16|2|||
| |- HysteresisOff|O3EInt16|2|||
**2417**|**MixerOneCircuitTargetValueRelativeHumidityCooling**|RawCodec|6|||
**2418**|**MixerTwoCircuitTargetValueRelativeHumidityCooling**|RawCodec|6|||
**2419**|**MixerThreeCircuitTargetValueRelativeHumidityCooling**|RawCodec|6|||
**2420**|**MixerFourCircuitTargetValueRelativeHumidityCooling**|RawCodec|6|||
**2421**|**MixerOneCircuitTemperatureOffsetCooling**|RawCodec|2|||
**2422**|**MixerTwoCircuitTemperatureOffsetCooling**|RawCodec|2|||
**2423**|**MixerThreeCircuitTemperatureOffsetCooling**|RawCodec|2|||
**2424**|**MixerFourCircuitTemperatureOffsetCooling**|RawCodec|2|||
**2425**|**BatteryModuleTypeId**|RawCodec|2|||
**2426**|**MixerOneCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6|||
| |- State|O3EBool|1|||
| |- OutsideTemperatureLimit|O3EInt16|2|||
| |- Unknown|O3EByteVal|1|||
| |- RoomTemperatureLimit|O3EInt16|2|||
**2427**|**MixerTwoCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6|||
| |- State|O3EBool|1|||
| |- OutsideTemperatureLimit|O3EInt16|2|||
| |- Unknown|O3EByteVal|1|||
| |- RoomTemperatureLimit|O3EInt16|2|||
**2428**|**MixerThreeCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6|||
| |- State|O3EBool|1|||
| |- OutsideTemperatureLimit|O3EInt16|2|||
| |- Unknown|O3EByteVal|1|||
| |- RoomTemperatureLimit|O3EInt16|2|||
**2429**|**MixerFourCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6|||
| |- State|O3EBool|1|||
| |- OutsideTemperatureLimit|O3EInt16|2|||
| |- Unknown|O3EByteVal|1|||
| |- RoomTemperatureLimit|O3EInt16|2|||
**2442**|**HeatPumpFrostProtection**|O3EInt8|1|||
**2444**|**LogLevelEmbbededApplication**|O3EInt8|1|||
**2445**|**SupplementalHeatEngineConfiguration**|RawCodec|2|||
**2446**|**HmiWakeupTrigger**|RawCodec|4|||
**2447**|**SupplyAirVolumeFlowDeviceLimit**|*O3EComplexType*|4|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
**2448**|**ExhaustAirVolumeFlowDeviceLimit**|*O3EComplexType*|4|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
**2449**|**CustomerSpecificDeviceName**|RawCodec|2|||
**2450**|**CascadeSequenceCurrentBoiler**|RawCodec|16|||
**2451**|**CascadeEmergencyOperationMode**|RawCodec|3|||
**2452**|**MixerOneCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4|||
| |- RoomHysteresisOn|O3EInt16|2|||
| |- RoomHysteresisOff|O3EInt16|2|||
**2453**|**MixerTwoCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4|||
| |- RoomHysteresisOn|O3EInt16|2|||
| |- RoomHysteresisOff|O3EInt16|2|||
**2454**|**MixerThreeCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4|||
| |- RoomHysteresisOn|O3EInt16|2|||
| |- RoomHysteresisOff|O3EInt16|2|||
**2455**|**MixerFourCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4|||
| |- RoomHysteresisOn|O3EInt16|2|||
| |- RoomHysteresisOff|O3EInt16|2|||
**2457**|**CalculatedOutsideTemperature**|*O3EComplexType*|9|||
| |- DampedActual|O3EInt16|2|||
| |- DampedMin|O3EInt16|2|||
| |- DampedMax|O3EInt16|2|||
| |- DampedAverage|O3EInt16|2|||
| |- Unknown|RawCodec|1|||
**2458**|**CascadeDeviceStatusLead**|RawCodec|18|||
**2459**|**CascadeDeviceStatusLagOne**|RawCodec|18|||
**2460**|**CascadeDeviceStatusLagTwo**|RawCodec|18|||
**2461**|**CascadeDeviceStatusLagThree**|RawCodec|18|||
**2462**|**CascadeDeviceStatusLagFour**|RawCodec|18|||
**2463**|**CascadeDeviceStatusLagFive**|RawCodec|18|||
**2464**|**CascadeDeviceStatusLagSix**|RawCodec|18|||
**2465**|**CascadeDeviceStatusLagSeven**|RawCodec|18|||
**2466**|**CascadeDeviceStatusLagEight**|RawCodec|18|||
**2467**|**CascadeDeviceStatusLagNine**|RawCodec|18|||
**2468**|**CascadeDeviceStatusLagTen**|RawCodec|18|||
**2469**|**CascadeDeviceStatusLagEleven**|RawCodec|18|||
**2470**|**CascadeDeviceStatusLagTwelve**|RawCodec|18|||
**2471**|**CascadeDeviceStatusLagThirteen**|RawCodec|18|||
**2472**|**CascadeDeviceStatusLagFourteen**|RawCodec|18|||
**2473**|**CascadeDeviceStatusLagFifteen**|RawCodec|18|||
**2474**|**CascadeCommonFlowTemperatureSensor**|RawCodec|9|||
**2475**|**CascadeCommonFlowCurrentTemperatureSetpoint**|O3EInt16|2|||
**2476**|**EnvironmentAirQualityTargetValues**|RawCodec|21|||
**2477**|**EnvironmentAirQualitySensor**|O3EByteVal|1|||
**2479**|**MixerOneCircuitRoomAirHumiditySensor**|RawCodec|5|||
**2480**|**MixerTwoCircuitRoomAirHumiditySensor**|RawCodec|5|||
**2481**|**MixerThreeCircuitRoomAirHumiditySensor**|RawCodec|5|||
**2482**|**MixerFourCircuitRoomAirHumiditySensor**|RawCodec|5|||
**2484**|**ElectricalPowerRangeMetaData**|RawCodec|8|||
**2486**|**CurrentElectricalPowerConsumptionRefrigerantCircuit**|O3EInt32|4|||
**2487**|**CurrentElectricalPowerConsumptionElectricHeater**|O3EInt32|4|||
**2488**|**CurrentElectricalPowerConsumptionSystem**|O3EInt32|4|||
**2489**|**FrostProtectionStatus**|RawCodec|3|||
**2490**|**StartUpWizardState**|RawCodec|1|||
**2491**|**DomesticHotWaterDemandInput**|RawCodec|1|||
**2493**|**VentilationBypassPosition**|RawCodec|2|||
**2494**|**CurrentThermalCapacityRefrigerantCircuit**|O3EInt32|4|||
**2495**|**CurrentThermalCapacityElectricHeater**|O3EInt32|4|||
**2496**|**CurrentThermalCapacitySystem**|O3EInt32|4|||
**2497**|**ResetStatisticalValuesDate**|RawCodec|3|||
**2498**|**CentralHeatingPumpType**|O3EByteVal|1|||
**2499**|**MixerOneCircuitPumpType**|O3EByteVal|1|||
**2500**|**MixerTwoCircuitPumpType**|O3EByteVal|1|||
**2501**|**MixerThreeCircuitPumpType**|O3EByteVal|1|||
**2502**|**MixerFourCircuitPumpType**|O3EByteVal|1|||
**2515**|**EnergyConsumptionDomesticHotWaterMonthMatrixElectricHeater**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**2516**|**EnergyConsumptionDomesticHotWaterYearMatrixElectricHeater**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**2517**|**EnergyConsumptionDomesticHotWaterElectricHeater**|*O3EComplexType*|24|||
| |- Today|O3EInt32|4|||
| |- Past7Days|O3EInt32|4|||
| |- CurrentMonth|O3EInt32|4|||
| |- PastMonth|O3EInt32|4|||
| |- CurrentYear|O3EInt32|4|||
| |- PastYear|O3EInt32|4|||
**2524**|**EnergyConsumptionCentralHeatingMonthMatrixElectricHeater**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**2525**|**EnergyConsumptionCentralHeatingYearMatrixElectricHeater**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**2526**|**EnergyConsumptionCentralHeatingElectricHeater**|*O3EComplexType*|24|||
| |- Today|O3EInt32|4|||
| |- Past7Days|O3EInt32|4|||
| |- CurrentMonth|O3EInt32|4|||
| |- PastMonth|O3EInt32|4|||
| |- CurrentYear|O3EInt32|4|||
| |- PastYear|O3EInt32|4|||
**2527**|**GeneratedCoolingOutputMonthMatrix**|*O3EComplexType*|124|||
| |- CurrentMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
| |- LastMonth|*O3EList*|62|||
| |- - 01|O3EInt16|2|||
| |- - 02|O3EInt16|2|||
| |- - 03|O3EInt16|2|||
| |- - 04|O3EInt16|2|||
| |- - 05|O3EInt16|2|||
| |- - 06|O3EInt16|2|||
| |- - 07|O3EInt16|2|||
| |- - 08|O3EInt16|2|||
| |- - 09|O3EInt16|2|||
| |- - 10|O3EInt16|2|||
| |- - 11|O3EInt16|2|||
| |- - 12|O3EInt16|2|||
| |- - 13|O3EInt16|2|||
| |- - 14|O3EInt16|2|||
| |- - 15|O3EInt16|2|||
| |- - 16|O3EInt16|2|||
| |- - 17|O3EInt16|2|||
| |- - 18|O3EInt16|2|||
| |- - 19|O3EInt16|2|||
| |- - 20|O3EInt16|2|||
| |- - 21|O3EInt16|2|||
| |- - 22|O3EInt16|2|||
| |- - 23|O3EInt16|2|||
| |- - 24|O3EInt16|2|||
| |- - 25|O3EInt16|2|||
| |- - 26|O3EInt16|2|||
| |- - 27|O3EInt16|2|||
| |- - 28|O3EInt16|2|||
| |- - 29|O3EInt16|2|||
| |- - 30|O3EInt16|2|||
| |- - 31|O3EInt16|2|||
**2528**|**GeneratedCoolingOutputYearMatrix**|*O3EComplexType*|96|||
| |- CurrentYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
| |- LastYear|*O3EList*|48|||
| |- - 01_January|O3EInt32|4|||
| |- - 02_February|O3EInt32|4|||
| |- - 03_March|O3EInt32|4|||
| |- - 04_April|O3EInt32|4|||
| |- - 05_May|O3EInt32|4|||
| |- - 06_June|O3EInt32|4|||
| |- - 07_July|O3EInt32|4|||
| |- - 08_August|O3EInt32|4|||
| |- - 09_September|O3EInt32|4|||
| |- - 10_October|O3EInt32|4|||
| |- - 11_November|O3EInt32|4|||
| |- - 12_December|O3EInt32|4|||
**2529**|**GeneratedCoolingOutput**|*O3EComplexType*|24|||
| |- Today|O3EInt32|4|||
| |- Past7Days|O3EInt32|4|||
| |- CurrentMonth|O3EInt32|4|||
| |- PastMonth|O3EInt32|4|||
| |- CurrentYear|O3EInt32|4|||
| |- PastYear|O3EInt32|4|||
**2533**|**PowerGridCodeSettingsNormSix**|RawCodec|27|||
**2534**|**BusTopologyMatrixSix**|RawCodec|181|||
**2535**|**BusTopologyMatrixSeven**|RawCodec|181|||
**2536**|**BusTopologyMatrixEight**|RawCodec|181|||
**2537**|**BusTopologyMatrixNine**|RawCodec|181|||
**2538**|**BusTopologyMatrixTen**|RawCodec|181|||
**2539**|**AlternatingCurrentEnergyStatistic**|RawCodec|40|||
**2540**|**NoiseReductionSettings**|RawCodec|6|||
**2541**|**SupplyAirVolumeFlowConfigurationLimit**|*O3EComplexType*|4|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
**2542**|**ExhaustAirVolumeFlowConfigurationLimit**|*O3EComplexType*|4|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
**2543**|**SmartGridTemperatureOffsets**|*O3EComplexType*|10|||
| |- SetpointIncreaseRoomTemperatureHeating|O3EInt16|2|||
| |- SetpointDecreaseRoomTemperatureCooling|O3EInt16|2|||
| |- SetpointIncreaseDHWTemperature|O3EInt16|2|||
| |- SetpointIncreaseBufferTemperatureHeating|O3EInt16|2|||
| |- SetpointDecreaseBufferTemperatureCooling|O3EInt16|2|||
**2544**|**EnableElectricalHeaterSmartGridLock**|O3EByteVal|1|||
**2545**|**EnableElectricalHeaterSmartGridIncreaseMaxDemand**|O3EByteVal|1|||
**2546**|**MixerOneCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Normal|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Unknown|O3EInt16|2|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**2547**|**MixerTwoCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Normal|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Unknown|O3EInt16|2|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**2548**|**MixerThreeCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Normal|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Unknown|O3EInt16|2|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**2549**|**MixerFourCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9|||
| |- Comfort|O3EInt16|2|||
| |- Normal|O3EInt16|2|||
| |- Reduced|O3EInt16|2|||
| |- Unknown|O3EInt16|2|||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1|||
**2551**|**FlameBurnerTwo**|RawCodec|6|||
**2552**|**ModulationCurrentValueBurnerTwo**|RawCodec|2|||
**2553**|**HeatEngineStatisticalBurnerTwo**|RawCodec|12|||
**2554**|**CellularModemIdentification**|RawCodec|62|||
**2555**|**ElectricalPowerSetPoint**|RawCodec|4|||
**2556**|**ElectricalEnergyRemainingCapacity**|RawCodec|4|||
**2557**|**HeatPumpState**|O3EByteVal|1|||
**2558**|**HeatPumpSupportedStates**|RawCodec|3|||
**2559**|**VentilationFanModbusId**|RawCodec|2|||
**2560**|**SmartGridFeatureSelection**|O3EByteVal|1|||
**2563**|**ZigBeeDeviceDecoupleList**|RawCodec|91|||
**2564**|**HydraulicFlapState**|RawCodec|1|||
**2566**|**VentilationSupplyFanRuntime**|O3EInt32|4|||
**2567**|**VentilationExhaustFanRuntime**|O3EInt32|4|||
**2568**|**RefrigerantType**|O3EInt8|1|||
**2569**|**CompressorSpeedRps**|O3EInt16|2|||
**2570**|**CompressorModulType**|O3EInt16|2|||
**2571**|**CompressorSuctionSuperheat**|O3EInt16|2|||
**2572**|**ActualCompressorInletMassflow**|RawCodec|4|||
**2573**|**CompressorOnTimer**|RawCodec|2|||
**2574**|**NominalPowerElectricalHeater**|*O3EComplexType*|8|||
| |- Power|O3EInt16|2|||
| |- Unknown|RawCodec|6|||
**2575**|**RefrigerationCycleApplicationState**|O3EInt16|2|||
**2576**|**FuelCellTestModeOne**|RawCodec|2|||
**2577**|**FuelCellTestModeTwo**|RawCodec|6|||
**2578**|**RefrigerationCircuitDesiredOperatingMode**|O3EInt8|1|||
**2579**|**CompressorMinMaxAllowedPrimaryTemperatureHeating**|RawCodec|4|||
**2580**|**CompressorSetpointRps**|O3EInt16|2|||
**2581**|**CompressorCalculatedSetpointRps**|O3EInt16|2|||
**2582**|**CompressorOffTimer**|RawCodec|2|||
**2583**|**OxygenProbeProcessValuesBurnerOne**|RawCodec|15|||
**2584**|**OxygenProbeProcessValuesBurnerTwo**|RawCodec|15|||
**2586**|**DigitalOutputCooling**|RawCodec|2|||
**2587**|**BatteryModuleWarrantyDataListLastEntry**|RawCodec|5|||
**2588**|**BatteryModuleWarrantyDataListOne**|RawCodec|197|||
**2589**|**BatteryModuleWarrantyDataListTwo**|RawCodec|197|||
**2590**|**HeatPumpCommonSettingsHeating**|RawCodec|8|||
**2591**|**HeatPumpCommonSettingsCooling**|RawCodec|8|||
**2592**|**ExpansionValveTheoreticalSetpoint**|RawCodec|4|||
**2593**|**ProductMatrix**|*O3EList*|181|||
| |- Count|O3EInt8|1|||
| |- - Unknown|RawCodec|2|||
| |- - VIN|O3EUtf8|16|||
**2594**|**ElectricalPreHeaterMonthMatrix**|RawCodec|124|||
**2595**|**ElectricalPreHeaterYearMatrix**|RawCodec|96|||
**2598**|**VentilationFanAssignmentAvailable**|O3EByteVal|1|||
**2599**|**VentilationFanAssignmentSwitch**|O3EByteVal|1|||
**2600**|**ElectricalHeaterActivation**|RawCodec|2|||
**2601**|**ElectricalHeaterVentilationConfiguration**|RawCodec|2|||
**2602**|**PrimaryHeatExchangerStatus**|RawCodec|10|||
**2603**|**PrimaryHeatExchangerCommonSettings**|RawCodec|4|||
**2604**|**LevelSwitchActivation**|O3EByteVal|1|||
**2605**|**QuickModeRuntime**|*O3EComplexType*|4|||
| |- NoiseReduced|O3EInt16|2|||
| |- Intensive|O3EInt16|2|||
**2606**|**ExternalTriggerActivation**|O3EByteVal|1|||
**2607**|**ExternalTriggerSettings**|O3EByteVal|1|||
**2608**|**FilterSettings**|RawCodec|28|||
**2609**|**CommissioningStatus**|RawCodec|6|||
**2610**|**SetDeliveryStateExpert**|RawCodec|1|||
**2611**|**NominalThermalCapacityIndoorUnit**|O3EInt32|4|||
**2612**|**PrimarySourceCommonSettingsHeating**|*O3EComplexType*|7|||
| |- Mode|O3EByteVal|1|||
| |- MaxFanSpeed|O3EInt16|2|||
| |- DefaultFanSpeed|O3EInt16|2|||
| |- MinFanSpeed|O3EInt16|2|||
**2613**|**PrimarySourceCommonSettingsCooling**|*O3EComplexType*|7|||
| |- Mode|O3EByteVal|1|||
| |- MaxFanSpeed|O3EInt16|2|||
| |- DefaultFanSpeed|O3EInt16|2|||
| |- MinFanSpeed|O3EInt16|2|||
**2621**|**MaximumOperatingPressureActualTemperatureSetpoint**|O3EInt16|2|||
**2622**|**SeasonalCoefficientOfPerformanceHeating**|*O3EComplexType*|9|||
| |- CurrentYear|O3EInt8|1|||
| |- EnergyThermal|O3EInt32|4|||
| |- EnergyElectric|O3EInt32|4|||
**2623**|**SeasonalEnergyEfficiencyRatioCooling**|*O3EComplexType*|9|||
| |- CurrentYear|O3EInt8|1|||
| |- EnergyThermal|O3EInt32|4|||
| |- EnergyElectric|O3EInt32|4|||
**2624**|**SeasonalCoefficientOfPerformanceDomesticHotWater**|*O3EComplexType*|9|||
| |- CurrentYear|O3EInt8|1|||
| |- EnergyThermal|O3EInt32|4|||
| |- EnergyElectric|O3EInt32|4|||
**2625**|**SeasonalCoefficientOfPerformanceHeatingAndDomesticHotWater**|*O3EComplexType*|9|||
| |- CurrentYear|O3EInt8|1|||
| |- EnergyThermal|O3EInt32|4|||
| |- EnergyElectric|O3EInt32|4|||
**2626**|**MaximumPowerElectricalHeater**|O3EInt32|4|||
**2627**|**CompressorStartUpTimer**|O3EInt16|2|||
**2629**|**DesiredThermalCapacity**|O3EInt32|4|||
**2630**|**CompressorMinMaxSpeedHeating**|*O3EComplexType*|4|||
| |- Min|O3EInt16|2|||
| |- Max|O3EInt16|2|||
**2631**|**CompressorMinMaxSpeedCooling**|*O3EComplexType*|4|||
| |- Min|O3EInt16|2|||
| |- Max|O3EInt16|2|||
**2632**|**CompressorMinMaxSpeedDefrost**|*O3EComplexType*|4|||
| |- Min|O3EInt16|2|||
| |- Max|O3EInt16|2|||
**2633**|**MaxSpeedNoiseReductionMode**|RawCodec|12|||
**2634**|**NoiseReductionMode**|O3EByteVal|1|||
**2635**|**BurnerProcessDataFlags**|RawCodec|8|||
**2636**|**BurnerTwoProcessDataFlags**|RawCodec|8|||
**2637**|**BurnerThreeProcessDataFlags**|RawCodec|8|||
**2638**|**SupportedCountryCodes**|RawCodec|4|||
**2643**|**MaximumRechargePower**|O3EInt16|2|||
**2733**|**InstallationConfirmation**|RawCodec|3|||
**2735**|**FourThreeWayValveValveCurrentPosition**|O3EByteVal|1|||
**2741**|**ComfortEnsuringMode**|RawCodec|3|||
**2742**|**DiagnosticHydraulicFilterInterval**|O3EInt8|1|||
**2743**|**DiagnosticElectricalHeaterSafetyTemperatureLimiter**|O3EInt8|1|||
**2744**|**DiagnosticSecondaryFourThreeWayValve**|O3EInt8|1|||
**2745**|**DiagnosticHydraulicFilterContamination**|O3EInt8|1|||
**2746**|**DiagnosticHydraulicSafetyValve**|O3EInt8|1|||
**2748**|**DiagnosticControlledLowPressureShutDown**|O3EInt8|1|||
**2749**|**DiagnosticControlledHighPressureShutDown**|O3EInt8|1|||
**2750**|**DiagnosticHydraulicTemperatureSensors**|O3EInt8|1|||
**2751**|**DiagnosticElectronicExpansionValve**|O3EInt8|1|||
**2752**|**DiagnosticFanOperation**|O3EInt8|1|||
**2753**|**DiagnosticHeatExchangerConstraints**|O3EInt8|1|||
**2758**|**GasPressureSwitchErrorReaction**|RawCodec|1|||
**2759**|**EnergyRecoveredCrossHeatExchanger**|RawCodec|24|||
**2760**|**EnergyOwnConsumption**|RawCodec|24|||
**2767**|**DiagnosticMonitoringPressureDrop**|O3EInt8|1|||
**2768**|**DiagnosticMonitoringPressurePeaks**|O3EInt8|1|||
**2772**|**EnergyRecoveredCrossHeatExchangerMonthMatrix**|RawCodec|124|||
**2773**|**EnergyRecoveredCrossHeatExchangerYearMatrix**|RawCodec|96|||
**2774**|**EnergyOwnConsumptionMonthMatrix**|RawCodec|124|||
**2775**|**EnergyOwnConsumptionYearMatrix**|RawCodec|96|||
**2776**|**ProductMatrixTwo**|RawCodec|181|||
**2777**|**PrimaryBootLoaderVersion**|RawCodec|8|||
**2778**|**ErrorMessageInputSelection**|RawCodec|2|||
**2779**|**DeltaTemperaturePumpControlSetpoint**|RawCodec|2|||
**2780**|**DomesticHotWaterFlowRangeDwellDuration**|RawCodec|1|||
**2781**|**AirVolumeFlowSetpoint**|RawCodec|7|||
**2782**|**AirVolumeFlowStatus**|RawCodec|24|||
**2783**|**VentilationSelfCheckDuration**|RawCodec|4|||
**2784**|**SecondaryHeatExchangerVaporPressureSensor**|*O3EComplexType*|9|||
| |- Pressure|O3EInt16|2|||
| |- Unknown|RawCodec|7|||
**2785**|**ElectricalHeaterStarts**|RawCodec|16|||
**2786**|**ElectricalPreheaterCurrentPowerConsumption**|RawCodec|2|||
**2791**|**CentralHeatingPumpStatus**|*O3EComplexType*|5|||
| |- Actual|O3EInt8|1|||
| |- Unknown|RawCodec|4|||
**2792**|**MixerOneCircuitPumpStatus**|*O3EComplexType*|5|||
| |- Actual|O3EInt8|1|||
| |- Unknown|RawCodec|4|||
**2793**|**MixerTwoCircuitPumpStatus**|*O3EComplexType*|5|||
| |- Actual|O3EInt8|1|||
| |- Unknown|RawCodec|4|||
**2794**|**MixerThreeCircuitPumpStatus**|*O3EComplexType*|5|||
| |- Actual|O3EInt8|1|||
| |- Unknown|RawCodec|4|||
**2795**|**MixerFourCircuitPumpStatus**|*O3EComplexType*|5|||
| |- Actual|O3EInt8|1|||
| |- Unknown|RawCodec|4|||
**2796**|**ExternalHeaterConfiguration**|*O3EComplexType*|2|||
| |- StateRoomHeating|O3EBool|1|||
| |- StateDHWHeating|O3EBool|1|||
**2797**|**VentilationBypassFlapAvailableCount**|O3EByteVal|1|||
**2798**|**RelativeHumiditySensorSelection**|O3EByteVal|1|||
**2799**|**ElectricalHeatersShutdownDelay**|O3EByteVal|1|||
**2800**|**VentilationHeatExchangerType**|O3EByteVal|1|||
**2801**|**VentilationFanAssignmentSwitchManufacturing**|O3EByteVal|1|||
**2802**|**InverterSelfTestStatus**|RawCodec|6|||
**2804**|**InverterSelfTestResultTwo**|RawCodec|151|||
**2805**|**InverterSelfTestResultThree**|RawCodec|151|||
**2806**|**RefrigerationCircuitOperationMode**|*O3EComplexType*|2|||
| |- Mode|O3EByteVal|1|||
| |- State|O3EByteVal|1|||
**2807**|**InverterHousingTemperature**|RawCodec|9|||
**2808**|**InverterInternalPowerModuleTemperature**|RawCodec|9|||
**2809**|**PumpMinSpeedConfiguration**|RawCodec|1|||
**2810**|**CentralHeatingPumpFeedbackSignalHandlingMode**|RawCodec|1|||
**2826**|**FuelCellNetworkSystemProtectionErrorHistory**|RawCodec|40|||
**2827**|**FuelCellNetworkSystemProtectionParameters**|RawCodec|48|||
**2828**|**FuelCellSdCardRecording**|RawCodec|2|||
**2829**|**ProductIdentification**|RawCodec|20|||
**2830**|**EmergencyMode**|RawCodec|1|||
**2831**|**BivalenceControlAlternativeTemperature**|O3EInt16|2|||
**2832**|**BaseHeaterTimer**|RawCodec|4|||
**2833**|**BaseHeaterTimerMode**|O3EInt8|1|||
**2834**|**BaseHeaterTimerDuration**|O3EInt16|2|||
**2835**|**BaseHeaterTemperatureThreshold**|O3EInt16|2|||
**2836**|**SecondaryHeatExchangerMinimumVolumeFlowThreshold**|O3EInt16|2|||
**2837**|**SecondaryHeatExchangerOptimumTemperatureSpreadExponent**|O3EInt16|2|||
**2838**|**SecondaryHeatExchangerOptimumTemperatureSpreadHeating**|RawCodec|4|||
**2839**|**SecondaryHeatExchangerOptimumTemperatureSpreadCooling**|RawCodec|4|||
**2840**|**SecondaryHeatExchangerOptimumVolumeFlowDefrost**|O3EInt16|2|||
**2842**|**SecondaryHeatExchangerHxSubcooling**|O3EInt16|2|||
**2843**|**SecondaryHeatExchangerMinimumVolumeFlow**|O3EInt16|2|||
**2844**|**SecondaryHeatExchangerMinimumOutletTemperature**|O3EInt16|2|||
**2845**|**SecondaryHeatExchangerMaximumOutletTemperature**|O3EInt16|2|||
**2847**|**CrankCaseHeaterStatistics**|RawCodec|8|||
**2848**|**CrankCaseHeaterTemperatureStatistics**|O3EInt16|2|||
**2849**|**CrankCaseHeaterOnTimer**|RawCodec|27|||
**2850**|**InstalledHeater**|*O3EComplexType*|3|||
| |- [FanDuctHeater](## "{0: Not Available, 1: Not Installed, 2: Installed, 3: Factory Installed}")|O3EEnum|1|||
| |- [CrankCaseHeater](## "{0: Not Available, 1: Not Installed, 2: Installed, 3: Factory Installed}")|O3EEnum|1|||
| |- [BaseHeater](## "{0: Not Available, 1: Not Installed, 2: Installed, 3: Factory Installed}")|O3EEnum|1|||
**2851**|**PreStartDuration**|O3EInt16|2|||
**2852**|**FanDuctHeater**|O3EByteVal|1|||
**2853**|**ExternalHeaterTimeIntegralThershold**|O3EInt16|2|||
**2855**|**MixerOneCircuitFrostProtectionConfiguration**|*O3EComplexType*|3|||
| |- State|O3EByteVal|1|||
| |- Temperature|O3EInt16|2|||
**2856**|**MixerTwoCircuitFrostProtectionConfiguration**|*O3EComplexType*|3|||
| |- State|O3EByteVal|1|||
| |- Temperature|O3EInt16|2|||
**2857**|**MixerThreeCircuitFrostProtectionConfiguration**|*O3EComplexType*|3|||
| |- State|O3EByteVal|1|||
| |- Temperature|O3EInt16|2|||
**2858**|**MixerFourCircuitFrostProtectionConfiguration**|*O3EComplexType*|3|||
| |- State|O3EByteVal|1|||
| |- Temperature|O3EInt16|2|||
**2874**|**PrimarySourceRpsOne**|O3EInt16|2|||
**2875**|**PrimarySourceRpsTwo**|O3EInt16|2|||
**2876**|**PrimaryPumpCommonSetpoint**|O3EInt16|2|||
**2877**|**SuctionSuperheatSetpoint**|O3EInt16|2|||
**2878**|**SubcoolingSetpoint**|O3EInt16|2|||
**2879**|**MixerOneCircuitHeatingBlocked**|RawCodec|2|||
**2880**|**MixerTwoCircuitHeatingBlocked**|RawCodec|2|||
**2881**|**ExpansionValveOneTimer**|RawCodec|4|||
**2882**|**ExpansionValveTwoTimer**|RawCodec|4|||
**2883**|**ExpansionValveMaximumOperatingPressureTemperatureSetpoint**|O3EInt16|2|||
**2884**|**ExpansionValveOneStatus**|O3EInt16|2|||
**2885**|**ExpansionValveTwoStatus**|O3EInt16|2|||
**2886**|**RefrigerantCyclePostStopDuration**|O3EInt16|2|||
**2887**|**RefrigerantCycleAlarmPauseDuration**|O3EInt16|2|||
**2888**|**RefrigerantCyclePumpdownStoppingDelay**|O3EInt16|2|||
**2889**|**RefrigerantCycleTimers**|RawCodec|6|||
**2890**|**RefrigerantCyclePumpdownHoldTimer**|O3EInt16|2|||
**2891**|**RefrigerantCycleDefrostTimers**|RawCodec|6|||
**2892**|**RefrigerantCycleTransitionToHeatingTimer**|O3EInt16|2|||
**2893**|**RefrigerantCycleTransitionToCoolingTimer**|O3EInt16|2|||
**2894**|**RefrigerantCycleAvailability**|O3EByteVal|1|||
**2895**|**PrimaryPumpSettings**|RawCodec|5|||
**2896**|**PrimaryPumpOneStatus**|O3EInt8|1|||
**2897**|**PrimaryPumpTwoStatus**|O3EInt8|1|||
**2908**|**InverterModuleType**|O3EInt8|1|||
**2909**|**CompressorMinMaxRequestedSecondaryReturnTemperatureCooling**|RawCodec|4|||
**2910**|**CompressorMinMaxRequestedSecondaryReturnTemperaturePreStartDefrost**|RawCodec|4|||
**2911**|**CompressorMaximumRequestedSecondaryReturnTempDefrost**|O3EInt16|2|||
**2912**|**CompressorMaximumDischargeTemperature**|O3EInt16|2|||
**2913**|**CompressorMinimumAllowedSecondaryOutletTemperatureHeating**|O3EInt16|2|||
**2914**|**CompressorMinMaxAllowedPrimaryTemperatureCooling**|RawCodec|4|||
**2915**|**CompressorMaximumCondensingPressure**|O3EInt16|2|||
**2916**|**CompressorMaximumEvaporatingPressure**|O3EInt16|2|||
**2917**|**CompressorMinimumEvaporatingPressureHeating**|O3EInt16|2|||
**2918**|**CompressorMinimumEvaporatingPressureCooling**|O3EInt16|2|||
**2920**|**ExternalHeaterSpecification**|RawCodec|2|||
**2921**|**DiagnosticHydraulicFilterIntervalSettings**|RawCodec|2|||
**2922**|**DiagnosticHydraulicFilterIntervalTemporalSettings**|RawCodec|2|||
**2923**|**DiagnosticSecondaryFourThreeWayValveSettings**|RawCodec|6|||
**2924**|**DiagnosticHydraulicFilterContaminationSettings**|RawCodec|4|||
**2925**|**DiagnosticMonitoringPressurePeaksSettings**|RawCodec|2|||
**2926**|**DiagnosticMonitoringPressureDropSettings**|RawCodec|6|||
**2927**|**DiagnosticElectronicExpansionValveSettings**|O3EInt8|1|||
**2928**|**DiagnosticHeatExchangerConstraintsSettings**|O3EInt16|2|||
**2929**|**DiagnosticRefrigerantCircuitPressureSensors**|O3EInt8|1|||
**2930**|**DiagnosticRefrigerantCircuitFourTwoWayValve**|O3EInt8|1|||
**2931**|**DiagnosticRefrigerantCircuitTemperatureSensors**|O3EInt8|1|||
**2932**|**TimeCounterSinceLastReset**|RawCodec|4|||
**2934**|**CurrentElectricalSystemPowerSetpoint**|O3EInt32|4|||
**2936**|**ElectricalEnergyStorageSystemState**|RawCodec|3|||
**2937**|**SystemPumpConfiguration**|RawCodec|2|||
**2938**|**CascadeSystemPump**|RawCodec|4|||
**2939**|**PrimaryHeatExchangerLowEvaporatingTemperatureAlarmDelay**|O3EInt16|2|||
**2940**|**ExternalHeaterDelayTimer**|*O3EComplexType*|3|||
| |- SwitchOnDelay|O3EInt8|1|||
| |- MinRunTime|O3EInt8|1|||
| |- SwitchOffDelay|O3EInt8|1|||
**2942**|**ListOfLayerSettingServiceDevices**|RawCodec|137|||
**2944**|**NodeIdOnExternalCan**|O3EByteVal|1|||
**2945**|**PointOfCommonCouplingEnergyMeterConnectedPhases**|RawCodec|1|||
**2946**|**EnergyConsumptionElectricalPreHeater**|RawCodec|24|||
**2947**|**SleepModePrevention**|RawCodec|5|||
**2952**|**ListOfLayerSettingServiceDevicesTwo**|RawCodec|137|||
**2953**|**CascadeSystemConfigurationArray**|RawCodec|10|||
**2956**|**DeviceDigitalInputEightValue**|O3EInt8|1|||
**2957**|**DeviceDigitalInputNineValue**|O3EInt8|1|||
**2969**|**ElectronicControlUnitSafeStateStatus**|O3EByteVal|1|||
**2985**|**ExternalHeaterTemperatureSetpoint**|O3EInt16|2|||
**2986**|**ExternalHeaterOperationState**|O3EByteVal|1|||
**2987**|**RefrigerantCycleUnlock**|O3EInt8|1|||
**2996**|**BatteryAmbientTemperatureHistogramTwoPointFour**|RawCodec|40|||
**2997**|**BatteryTemperatureHistogramTwoPointFour**|RawCodec|56|||
**2998**|**HardwareSignalCheckCsc**|RawCodec|8|||
**2999**|**ElectricalHeatersOperationHours**|RawCodec|16|||
**3000**|**EcuResetInformationList**|RawCodec|115|||
**3001**|**LowEvaporatingLowCondensingDriveDuration**|RawCodec|196|||
**3002**|**MidEvaporatingLowCondensingDriveDuration**|RawCodec|196|||
**3003**|**HighEvaporatingLowCondensingDriveDuration**|RawCodec|196|||
**3004**|**LowEvaporatingHighCondensingDriveDuration**|RawCodec|196|||
**3005**|**MidEvaporatingHighCondensingDriveDuration**|RawCodec|196|||
**3006**|**HighEvaporatingHighCondensingDriveDuration**|RawCodec|196|||
**3008**|**FanDuctHeaterOnDuration**|O3EInt16|2|||
**3009**|**FanDuctHeaterOnTimer**|RawCodec|4|||
**3013**|**MixerHybridThreeWayValvePositionPercent**|RawCodec|2|||
**3014**|**OutdoorMiddleCoilTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3015**|**HeatSinkTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3016**|**HeatingBufferTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3017**|**CoolingBufferTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3018**|**HeatingCoolingBufferTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3019**|**CompressorOutletTargetTemperature**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3029**|**DomesticHotWaterEfficiencyMode**|O3EByteVal|1|||
**3030**|**DomesticHotWaterEfficiencyModeAvailability**|RawCodec|2|||
**3031**|**ExternalHeater**|RawCodec|2|||
**3032**|**PrimaryEnergyFactorElectricity**|O3EInt16|2|||
**3034**|**DomesticHotWaterReturnTemperaturTankLoadSystem**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3035**|**DomesticHotWaterFlowTemperaturTankLoadSystem**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3036**|**PrimaryEnergyFactorExternalHeater**|O3EInt16|2|||
**3037**|**ElectricityPriceTimeScheduleMonday**|RawCodec|57|||
**3038**|**ElectricityPriceTimeScheduleTuesday**|RawCodec|57|||
**3039**|**ElectricityPriceTimeScheduleWednesday**|RawCodec|57|||
**3040**|**ElectricityPriceTimeScheduleThursday**|RawCodec|57|||
**3041**|**ElectricityPriceTimeScheduleFriday**|RawCodec|57|||
**3042**|**ElectricityPriceTimeScheduleSaturday**|RawCodec|57|||
**3043**|**ElectricityPriceTimeScheduleSunday**|RawCodec|57|||
**3056**|**NarrowBandInternetOfThingsNetworkStatus**|O3EInt8|1|||
**3057**|**NarrowBandInternetOfThingsCloudStatus**|O3EInt8|1|||
**3066**|**DomesticHotWaterHighDemandDetection**|RawCodec|4|||
**3067**|**AirVolumeFlowValue**|RawCodec|9|||
**3068**|**DomesticHotWaterTemperatureSetpointComfort**|RawCodec|2|||
**3069**|**DomesticHotWaterSensorForDemand**|O3EByteVal|1|||
**3070**|**BufferTargetOperationMode**|O3EByteVal|1|||
**3085**|**ElectricalEnergyStorageModuleOneInformation**|RawCodec|18|||
**3086**|**ElectricalEnergyStorageModuleTwoInformation**|RawCodec|18|||
**3087**|**ElectricalEnergyStorageModuleThreeInformation**|RawCodec|18|||
**3088**|**ElectricalEnergyStorageModuleFourInformation**|RawCodec|18|||
**3089**|**ElectricalEnergyStorageModuleFiveInformation**|RawCodec|18|||
**3090**|**ElectricalEnergyStorageModuleSixInformation**|RawCodec|18|||
**3091**|**GatewayEthernetTwoEnable**|O3EByteVal|1|||
**3092**|**GatewayEthernetTwoConfig**|RawCodec|21|||
**3093**|**GatewayEthernetTwoIp**|RawCodec|20|||
**3094**|**GatewayEthernetTwoNetworkStatus**|O3EByteVal|1|||
**3095**|**MacAddressLanTwo**|RawCodec|6|||
**3096**|**GatewayWifiStationEnable**|O3EByteVal|1|||
**3097**|**GatewayInternetAccess**|O3EByteVal|1|||
**3098**|**ExternalHeaterTemperatureOffset**|*O3EComplexType*|2|||
| |- Offset|O3EInt8|1|||
| |- Unknown|RawCodec|1|||
**3103**|**IsCountryModeLoadInformation**|RawCodec|6|||
**3106**|**BufferMinimumMaximumSetTemperature**|*O3EComplexType*|4|||
| |- BufferMin|O3EInt16|2|||
| |- BufferMax|O3EInt16|2|||
**3107**|**BatteryModuleExchangeAssistent**|RawCodec|7|||
**3108**|**PhotovoltaicsActivePowerLimitationRampRate**|RawCodec|9|||
**3109**|**PrimaryHeatExchangerBaseHeaterStatistical**|RawCodec|8|||
**3113**|**DeviceDigitalOutputOneValueStatistical**|RawCodec|8|||
**3114**|**DeviceDigitalOutputTwoValueStatistical**|RawCodec|8|||
**3115**|**DeviceDigitalOutputThreeValueStatistical**|RawCodec|8|||
**3116**|**DeviceDigitalOutputFourValueStatistical**|RawCodec|8|||
**3117**|**DeviceDigitalOutputFiveValueStatistical**|RawCodec|8|||
**3119**|**RefrigerantCircuitFourWayValveStatistical**|RawCodec|8|||
**3120**|**CompressorCrankCaseHeaterStatistical**|RawCodec|8|||
**3129**|**FanDuctHeaterStatistical**|RawCodec|8|||
**3134**|**DomesticHotWaterCirculationPumpStatistical**|RawCodec|8|||
**3146**|**ElectricalHeaterPhaseOneStatistical**|RawCodec|8|||
**3147**|**ElectricalHeaterPhaseTwoStatistical**|RawCodec|8|||
**3148**|**ElectricalHeaterPhaseThreeStatistical**|RawCodec|8|||
**3155**|**DomesticHotWaterShiftLoadPumpStatus**|RawCodec|5|||
**3156**|**DomesticHotWaterShiftLoadPumpType**|O3EByteVal|1|||
**3190**|**RefrigerantCircuitFourWayValvePosition**|O3EByteVal|1|||
**3191**|**ExtendedEventLoggingHistory**|RawCodec|199|||
**3212**|**BivalentMixerDomesticHotWaterTemperatureOffset**|*O3EComplexType*|2|||
| |- Offset|O3EInt8|1|||
| |- Unknown|RawCodec|1|||
**3213**|**ExternalHeaterTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3215**|**ExternalHeaterSeparatorTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3228**|**EnergyMeterOne**|*O3EComplexType*|73|||
| |- PowerL1|O3EInt32|4|||
| |- ReactivePowerL1|O3EInt32|4|||
| |- PowerL2|O3EInt32|4|||
| |- ReactivePowerL2|O3EInt32|4|||
| |- PowerL3|O3EInt32|4|||
| |- ReactivePowerL3|O3EInt32|4|||
| |- EnergyImport|O3EInt64|8|||
| |- EnergyExport|O3EInt64|8|||
| |- Unknown1|O3EInt64|8|||
| |- Unknown2|RawCodec|8|||
| |- VoltageL1|O3EInt16|2|||
| |- VoltageL2|O3EInt16|2|||
| |- VoltageL3|O3EInt16|2|||
| |- CurrentL1|O3EInt16|2|||
| |- CurrentL2|O3EInt16|2|||
| |- CurrentL3|O3EInt16|2|||
| |- PowerFactor|O3EInt16|2|||
| |- Unknown3|RawCodec|3|||
**3229**|**EnergyMeterTwo**|*O3EComplexType*|73|||
| |- PowerL1|O3EInt32|4|||
| |- ReactivePowerL1|O3EInt32|4|||
| |- PowerL2|O3EInt32|4|||
| |- ReactivePowerL2|O3EInt32|4|||
| |- PowerL3|O3EInt32|4|||
| |- ReactivePowerL3|O3EInt32|4|||
| |- EnergyImport|O3EInt64|8|||
| |- EnergyExport|O3EInt64|8|||
| |- Unknown1|O3EInt64|8|||
| |- Unknown2|RawCodec|8|||
| |- VoltageL1|O3EInt16|2|||
| |- VoltageL2|O3EInt16|2|||
| |- VoltageL3|O3EInt16|2|||
| |- CurrentL1|O3EInt16|2|||
| |- CurrentL2|O3EInt16|2|||
| |- CurrentL3|O3EInt16|2|||
| |- PowerFactor|O3EInt16|2|||
| |- Unknown3|RawCodec|3|||
**3230**|**EnergyMeterThree**|*O3EComplexType*|73|||
| |- PowerL1|O3EInt32|4|||
| |- ReactivePowerL1|O3EInt32|4|||
| |- PowerL2|O3EInt32|4|||
| |- ReactivePowerL2|O3EInt32|4|||
| |- PowerL3|O3EInt32|4|||
| |- ReactivePowerL3|O3EInt32|4|||
| |- EnergyImport|O3EInt64|8|||
| |- EnergyExport|O3EInt64|8|||
| |- Unknown1|O3EInt64|8|||
| |- Unknown2|RawCodec|8|||
| |- VoltageL1|O3EInt16|2|||
| |- VoltageL2|O3EInt16|2|||
| |- VoltageL3|O3EInt16|2|||
| |- CurrentL1|O3EInt16|2|||
| |- CurrentL2|O3EInt16|2|||
| |- CurrentL3|O3EInt16|2|||
| |- PowerFactor|O3EInt16|2|||
| |- Unknown3|RawCodec|3|||
**3231**|**EnergyMeterFour**|*O3EComplexType*|73|||
| |- PowerL1|O3EInt32|4|||
| |- ReactivePowerL1|O3EInt32|4|||
| |- PowerL2|O3EInt32|4|||
| |- ReactivePowerL2|O3EInt32|4|||
| |- PowerL3|O3EInt32|4|||
| |- ReactivePowerL3|O3EInt32|4|||
| |- EnergyImport|O3EInt64|8|||
| |- EnergyExport|O3EInt64|8|||
| |- Unknown1|O3EInt64|8|||
| |- Unknown2|RawCodec|8|||
| |- VoltageL1|O3EInt16|2|||
| |- VoltageL2|O3EInt16|2|||
| |- VoltageL3|O3EInt16|2|||
| |- CurrentL1|O3EInt16|2|||
| |- CurrentL2|O3EInt16|2|||
| |- CurrentL3|O3EInt16|2|||
| |- PowerFactor|O3EInt16|2|||
| |- Unknown3|RawCodec|3|||
**3234**|**DomesticHotWaterBufferTopTemperatureSensor**|*O3EComplexType*|9|||
| |- Actual|O3EInt16|2|||
| |- Minimum|O3EInt16|2|||
| |- Maximum|O3EInt16|2|||
| |- Average|O3EInt16|2|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1|||
**3335**|**HeatingCoolingHysteresisHeatingCircuitOne**|*O3EComplexType*|8|||
| |- TurnOnHysteresis_Heating|O3EInt16|2|||
| |- TurnOffHysteresis_Heating|O3EInt16|2|||
| |- TurnOnHysteresis_Cooling|O3EInt16|2|||
| |- TurnOffHysteresis_Cooling|O3EInt16|2|||
**3336**|**HeatingCoolingHysteresisHeatingCircuitTwo**|*O3EComplexType*|8|||
| |- TurnOnHysteresis_Heating|O3EInt16|2|||
| |- TurnOffHysteresis_Heating|O3EInt16|2|||
| |- TurnOnHysteresis_Cooling|O3EInt16|2|||
| |- TurnOffHysteresis_Cooling|O3EInt16|2|||
**3337**|**HeatingCoolingHysteresisHeatingCircuitThree**|*O3EComplexType*|8|||
| |- TurnOnHysteresis_Heating|O3EInt16|2|||
| |- TurnOffHysteresis_Heating|O3EInt16|2|||
| |- TurnOnHysteresis_Cooling|O3EInt16|2|||
| |- TurnOffHysteresis_Cooling|O3EInt16|2|||
**3338**|**HeatingCoolingHysteresisHeatingCircuitFour**|*O3EComplexType*|8|||
| |- TurnOnHysteresis_Heating|O3EInt16|2|||
| |- TurnOffHysteresis_Heating|O3EInt16|2|||
| |- TurnOnHysteresis_Cooling|O3EInt16|2|||
| |- TurnOffHysteresis_Cooling|O3EInt16|2|||
**3366**|**ElectricalActivePowerStatusReport**|*O3EComplexType*|16|||
| |- 15MinPower|O3EInt32|4|||
| |- 15MinEnergy|O3EInt32|4|||
| |- Unknown1|O3EInt32|4|||
| |- Unknown2|O3EInt32|4|||
**3384**|**ElectricalActivePowerConsumptionLimitationDefaultValue**|*O3EComplexType*|4|||
| |- Default|O3EInt16|2|||
| |- CurrentValue|O3EInt16|2|||

