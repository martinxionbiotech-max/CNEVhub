#!/usr/bin/env python3
"""Build src/data/technical-master.json — P4 Technical Authority entity layer.

All entity names/definitions are web-verified (Wikipedia standards pages, official
OEM/CATL releases, EU regulation 2023/1542, standards bodies). No invented tech.
Run: python3 scripts/build_technical_master.py
"""
import json
import os
import sys

E = []


def add(eid, name, name_zh, category, definition, source, related_vehicles=None):
    ent = {
        "id": eid,
        "name": name,
        "name_zh": name_zh,
        "category": category,
        "definition": definition,
        "source": source,
    }
    if related_vehicles:
        ent["related_vehicles"] = related_vehicles
    E.append(ent)


WIKI_LFP = "Wikipedia, Lithium iron phosphate battery — https://en.wikipedia.org/wiki/Lithium_iron_phosphate_battery"
WIKI_NMC = "Wikipedia, Lithium nickel manganese cobalt oxide — https://en.wikipedia.org/wiki/Lithium_nickel_manganese_cobalt_oxide"
WIKI_NCA = "Wikipedia, Lithium nickel cobalt aluminium oxide — https://en.wikipedia.org/wiki/Lithium_nickel_cobalt_aluminium_oxide"
WIKI_NA = "Wikipedia, Sodium-ion battery — https://en.wikipedia.org/wiki/Sodium-ion_battery"
WIKI_SSB = "Wikipedia, Solid-state battery — https://en.wikipedia.org/wiki/Solid-state_battery"
WIKI_GB = "Wikipedia, GB/T charging standard — https://en.wikipedia.org/wiki/GB/T_charging_standard"
WIKI_CYL = "Wikipedia, Lithium-ion battery (cylindrical formats) — https://en.wikipedia.org/wiki/Lithium-ion_battery"
CATL_STD = "CATL official news, Super Technology Day / Naxtra Battery — https://www.catl.com/en/news/6401.html"
CATL_2026 = "CATL official news, Six Major Innovations — https://www.catl.com/en/news/6811.html"
EU_BATT = "European Commission, Regulation (EU) 2023/1542 Art. 77 & Annex XIII (battery passport, mandatory 18 Feb 2027)"

# ---------------------------------------------------------------- battery (35)
add("lfp-battery", "Lithium iron phosphate battery (LFP)", "磷酸铁锂电池 (LFP)", "battery",
    "Lithium-ion battery whose cathode is lithium iron phosphate (LiFePO4). It offers high thermal stability and long cycle life but lower energy density than nickel-based chemistries.",
    WIKI_LFP,
    ["byd-seal", "byd-dolphin", "byd-atto-3", "byd-han", "byd-seagull", "wuling-hongguang-mini-ev", "byd-song-plus", "leapmotor-c11"])
add("nmc-battery", "Nickel manganese cobalt battery (NMC)", "三元锂电池 (NMC)", "battery",
    "Lithium-ion battery using a layered nickel-manganese-cobalt oxide cathode; higher energy density and better cold-weather performance than LFP at higher cost.",
    WIKI_NMC,
    ["nio-et7", "zeekr-001", "avatr-12", "xiaomi-su7", "zeekr-009"])
add("nca-battery", "Nickel cobalt aluminium battery (NCA)", "镍钴铝电池 (NCA)", "battery",
    "Lithium-ion chemistry with a LiNiCoAlO2 cathode, known for very high energy density and used in early long-range EV packs.",
    WIKI_NCA)
add("lmfp-battery", "Lithium manganese iron phosphate battery (LMFP)", "磷酸锰铁锂电池 (LMFP)", "battery",
    "LFP variant with manganese doping that raises the operating voltage, delivering roughly 15-20% higher energy density than plain LFP while keeping olivine safety.",
    WIKI_LFP)
add("sodium-ion-battery", "Sodium-ion battery", "钠离子电池", "battery",
    "Rechargeable battery that shuttles sodium ions instead of lithium. It uses abundant, low-cost materials and performs well in cold weather but has lower energy density.",
    WIKI_NA,
    ["byd-dolphin", "byd-seagull"])
add("naxtra-battery", "CATL Naxtra sodium-ion battery", "宁德时代 Naxtra 钠新电池", "battery",
    "CATL's mass-produced sodium-ion EV battery, rated up to 175 Wh/kg with 5C peak charge and over 90% power retention at -40 degrees C; full-scale mass production targeted for end-2026.",
    CATL_STD)
add("solid-state-battery", "Solid-state battery", "全固态电池", "battery",
    "Battery in which the liquid electrolyte is replaced by a solid electrolyte, promising higher energy density and improved safety. Automotive volumes remain in pilot production as of 2026.",
    WIKI_SSB)
add("semi-solid-state-battery", "Semi-solid-state battery", "半固态电池", "battery",
    "Intermediate design using a gel or quasi-solid electrolyte with a small liquid fraction. It has already reached limited series production in long-range packs.",
    WIKI_SSB)
add("condensed-matter-battery", "CATL condensed-matter battery", "宁德时代凝聚态电池", "battery",
    "CATL high-energy cell built around a condensed electrolyte, announced at 350 Wh/kg at the cell level in 2026.",
    CATL_2026)
add("blade-battery", "BYD Blade Battery", "比亚迪刀片电池", "battery",
    "BYD's long, thin LFP cell (about 960 mm) designed as a structural pack element. Its nail-penetration test results show no fire or explosion.",
    "BYD official, Blade Battery — https://www.byd.com/en/news (see also ResearchInChina CTP/CTB/CTC report)",
    ["byd-han", "byd-seal", "byd-atto-3", "byd-dolphin", "byd-sealion-07"])
add("qilin-battery", "CATL Qilin battery", "宁德时代麒麟电池", "battery",
    "CATL's third-generation cell-to-pack battery with a system-level energy density of 255 Wh/kg and 72% pack volume utilisation.",
    CATL_2026)
add("shenxing-battery", "CATL Shenxing superfast charging battery", "宁德时代神行电池", "battery",
    "LFP battery line built for very high charge rates: the first generation supported 4C charging and later generations claim up to 12C peak, giving roughly 10-minute 10-80% charging.",
    CATL_STD)
add("freevoy-battery", "CATL Freevoy dual-power battery", "宁德时代骁遥双核电池", "battery",
    "Battery that blends LFP and NCM at the particle level, reaching about 230 Wh/kg and supporting pure-electric plus hybrid operation with combined range above 2,000 km.",
    CATL_2026)
add("ctp-cell-to-pack", "Cell-to-pack (CTP)", "电芯直接集成电池包 (CTP)", "battery",
    "Pack architecture that removes modules and places cells directly in the pack enclosure, cutting part count by roughly 40% and lifting volume utilisation to 60-70%.",
    "Frontiers in Mechanical Engineering, review of CTB battery-structure integration — https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1825484/full",
    ["byd-seal", "nio-et7", "zeekr-001"])
add("ctb-cell-to-body", "Cell-to-body (CTB)", "电池车身一体化 (CTB)", "battery",
    "Design in which the battery pack's upper cover replaces the car's floor, making the pack a load-bearing part of the body structure; introduced by BYD in 2022.",
    "ResearchInChina, Passenger Car CTP/CTC/CTB Integrated Battery Industry Report — https://www.researchinchina.com/Htmls/Report/2024/73951.html",
    ["byd-seal", "byd-han"])
add("ctc-cell-to-chassis", "Cell-to-chassis (CTC)", "电池底盘一体化 (CTC)", "battery",
    "Architecture in which cells are integrated directly into the vehicle chassis or underbody, so the battery enclosure acts as a floor panel or structural member.",
    "ResearchInChina, Passenger Car CTP/CTC/CTB Integrated Battery Industry Report — https://www.researchinchina.com/Htmls/Report/2024/73951.html")
add("ctm-cell-to-module", "Cell-to-module (CTM)", "电芯到模组 (CTM)", "battery",
    "Conventional pack architecture in which cells are first assembled into modules that are then installed in the pack, offering easier serviceability at lower volume efficiency.",
    "Bonnen Battery, EV battery pack designs from modules to body-integrated power — https://www.bonnenbatteries.com/ev-battery-pack-designs-from-modules-to-body-integrated-power")
add("cylindrical-4680-cell", "4680 cylindrical cell", "4680 大圆柱电芯", "battery",
    "Tesla's 46 mm diameter by 80 mm tall tabless cylindrical cell, claimed to deliver about five times the energy and six times the power of the 2170 format.",
    "Tesla Battery Day 2020 / Wikipedia, Tesla 4680 — https://en.wikipedia.org/wiki/Tesla_4680")
add("cylindrical-21700-cell", "21700 cylindrical cell", "21700 圆柱电芯", "battery",
    "21 mm diameter by 70 mm cylindrical lithium-ion cell format widely used in EV and power-tool packs.",
    WIKI_CYL)
add("cylindrical-18650-cell", "18650 cylindrical cell", "18650 圆柱电芯", "battery",
    "18 mm diameter by 65 mm cylindrical cell, the format that scaled early EV and consumer battery packs.",
    WIKI_CYL)
add("prismatic-cell", "Prismatic cell", "方形电芯", "battery",
    "Rectangular hard-cased cell format that dominates the Chinese EV market because it packages densely and resists swelling.",
    WIKI_CYL)
add("pouch-cell", "Pouch cell", "软包电芯", "battery",
    "Cell sealed in a laminated foil pouch; it has high packaging efficiency and low weight but needs external compression for mechanical support.",
    WIKI_CYL)
add("tabless-electrode", "Tabless electrode design", "无极耳(全极耳)设计", "battery",
    "Electrode construction that replaces discrete tabs with a continuous current-collector edge, shortening the current path to cut internal resistance and enable high-power cells.",
    "Tesla, Battery Day 2020 (tabless 4680 cell) — https://www.tesla.com/")
add("dry-electrode-process", "Dry battery electrode process", "干法电极工艺", "battery",
    "Solvent-free electrode manufacturing route that avoids large drying ovens, cutting factory energy use and floor space compared with wet slurry coating.",
    "Tesla, Battery Day 2020 (dry electrode process) — https://www.tesla.com/")
add("battery-management-system", "Battery management system (BMS)", "电池管理系统 (BMS)", "battery",
    "Electronics that monitor cell voltage and temperature, estimate state of charge and health, balance cells and enforce protection limits.",
    "Wikipedia, Battery management system — https://en.wikipedia.org/wiki/Battery_management_system")
add("soc-state-of-charge", "State of charge (SOC)", "荷电状态 (SOC)", "battery",
    "The remaining energy in a battery expressed as a percentage of its rated capacity; it governs usable range and charge-power limits.",
    "Wikipedia, State of charge — https://en.wikipedia.org/wiki/State_of_charge")
add("soh-state-of-health", "State of health (SOH)", "电池健康度 (SOH)", "battery",
    "Measure of a battery's current capacity and internal resistance relative to new condition. It is a required data point in the EU battery passport and a key input for used-EV valuation.",
    EU_BATT)
add("battery-passport", "EU battery passport", "欧盟电池护照", "battery",
    "Machine-readable digital record required by Regulation (EU) 2023/1542 for EV, LMT and industrial batteries above 2 kWh placed on the EU market from 18 February 2027, accessed by QR code and covering carbon footprint, recycled content, chemistry and state of health.",
    EU_BATT)
add("silicon-carbon-anode", "Silicon-carbon anode", "硅碳负极", "battery",
    "Anode that blends silicon into graphite to raise capacity beyond pure graphite; carbon scaffolding is used to buffer silicon's large volume expansion.",
    "Wikipedia, Lithium-ion battery (anode materials) — https://en.wikipedia.org/wiki/Lithium-ion_battery")
add("lithium-plating", "Lithium plating", "析锂", "battery",
    "Deposition of metallic lithium on the anode surface instead of intercalation, typically during fast charging at low temperature. It permanently consumes lithium and can seed dendrites.",
    "Wikipedia, Lithium-ion battery (degradation) — https://en.wikipedia.org/wiki/Lithium-ion_battery")
add("calendar-aging", "Calendar aging", "日历老化", "battery",
    "Capacity fade that occurs with time regardless of cycling, accelerated by high state of charge and high ambient temperature.",
    "Wikipedia, Lithium-ion battery (degradation) — https://en.wikipedia.org/wiki/Lithium-ion_battery")
add("thermal-runaway", "Thermal runaway", "热失控", "battery",
    "Self-sustaining exothermic chain reaction inside a cell that can propagate to neighbouring cells; the central failure mode that EV battery safety standards target.",
    "Wikipedia, Thermal runaway — https://en.wikipedia.org/wiki/Thermal_runaway")
add("lfp-thermal-stability", "LFP thermal stability", "磷酸铁锂热稳定性", "battery",
    "The strong P-O bonds and olivine structure of LFP raise its decomposition temperature, giving a longer time between failure onset and fire than nickel-rich chemistries.",
    WIKI_LFP,
    ["byd-han", "byd-seal", "byd-dolphin"])
add("c-rate", "C-rate", "充放电倍率 (C 率)", "battery",
    "Charge or discharge current normalised to battery capacity: 1C empties or fills the pack in one hour, 5C in about twelve minutes.",
    "Wikipedia, C-rate / battery capacity — https://en.wikipedia.org/wiki/Battery_charger#C-rate")
add("cobalt-free-battery", "Cobalt-free battery", "无钴电池", "battery",
    "Cathode design that avoids cobalt, either by using LFP/LMFP or nickel-manganese-only layered oxides, to reduce cost and supply-chain exposure.",
    WIKI_NMC)
add("second-life-battery", "Second-life battery", "电池梯次利用", "battery",
    "Repurposing of retired EV packs into stationary storage before recycling, extending service life and lowering the carbon cost per kWh.",
    "Wikipedia, Battery recycling (reuse and repurposing) — https://en.wikipedia.org/wiki/Battery_recycling")
add("battery-recycling-black-mass", "Black mass", "黑粉", "battery",
    "Shredded and separated battery output that concentrates cathode metals; it is the feedstock for hydrometallurgical recovery of nickel, cobalt and lithium.",
    "Wikipedia, Battery recycling — https://en.wikipedia.org/wiki/Battery_recycling")
add("energy-density-gravimetric", "Gravimetric energy density", "质量能量密度 (Wh/kg)", "battery",
    "Energy stored per unit mass, reported in Wh/kg at cell or pack level; the main lever on EV range for a given battery weight.",
    "Wikipedia, Energy density — https://en.wikipedia.org/wiki/Energy_density")
add("energy-density-volumetric", "Volumetric energy density", "体积能量密度 (Wh/L)", "battery",
    "Energy stored per unit volume in Wh/L; it determines how much battery fits into a fixed floor area.",
    "Wikipedia, Energy density — https://en.wikipedia.org/wiki/Energy_density")

# --------------------------------------------------------------- charging (31)
add("gbt-20234", "GB/T 20234 charging standard", "国标 GB/T 20234 充电标准", "charging",
    "Chinese national standard for EV charging connectors and interfaces: GB/T 20234.2 covers AC and GB/T 20234.3 covers DC. The 2023 revision extended DC charging up to 1,500 V and 800 A.",
    WIKI_GB,
    ["byd-seal", "nio-et7", "xpeng-g9", "aion-y"])
add("gbt-ac-connector", "GB/T AC charging connector", "国标交流充电接口", "charging",
    "Seven-pin AC connector defined by GB/T 20234.2, used for single- and three-phase AC charging in mainland China.",
    WIKI_GB)
add("gbt-dc-connector", "GB/T DC charging connector", "国标直流充电接口", "charging",
    "Nine-pin DC connector defined by GB/T 20234.3, mechanically incompatible with CCS and CHAdeMO so adapter hardware is required.",
    WIKI_GB)
add("gbt-27930", "GB/T 27930 communication protocol", "国标 GB/T 27930 通信协议", "charging",
    "CAN-based communication protocol (derived from SAE J1939) between an EV and a DC charger in China, corresponding to ISO 15118 in Western standards.",
    WIKI_GB)
add("gbt-18487", "GB/T 18487 conductive charging system", "国标 GB/T 18487 传导充电系统", "charging",
    "Chinese general requirements standard for conductive charging systems, corresponding to IEC 61851 in the international framework.",
    WIKI_GB)
add("ccs1", "Combined Charging System 1 (CCS1)", "北美 CCS1 充电标准", "charging",
    "North American DC standard combining the SAE J1772 Type 1 AC connector with two DC pins, supporting up to 350 kW at 1,000 V.",
    "PowerON EVSE, CCS1/CCS2/CHAdeMO/GB-T comparison — https://poweron-evse.com/ev-charging-insights/powering-the-future-a-deep-dive-into-ccs1-ccs2-chademo-and-gb-t-ev-charging-standards")
add("ccs2", "Combined Charging System 2 (CCS2)", "欧洲 CCS2 充电标准", "charging",
    "European DC standard pairing the IEC 62196 Type 2 AC connector with two DC pins, rated to 1,000 V and 500 A and the mandatory plug for EU public DC charging.",
    "PowerON EVSE, CCS1/CCS2/CHAdeMO/GB-T comparison — https://poweron-evse.com/ev-charging-insights/powering-the-future-a-deep-dive-into-ccs1-ccs2-chademo-and-gb-t-ev-charging-standards")
add("chademo", "CHAdeMO", "日本 CHAdeMO 快充标准", "charging",
    "DC fast charging standard introduced in Japan in 2010 by the CHAdeMO Association; the original 62.5 kW rating was later extended to 200 kW and beyond, and it supports bidirectional V2G.",
    "Driivz, EV charging standards and protocols — https://driivz.com/blog/ev-charging-standards-and-protocols")
add("nacs", "North American Charging Standard (NACS)", "北美充电标准 (NACS)", "charging",
    "Tesla-designed charging connector opened to the industry and standardised by SAE: a Technical Information Report was published in December 2023 and the J3400 Recommended Practice in September 2024. Most North American automakers have adopted it for DC fast charging.",
    "SAE International, SAE J3400 North American Charging System Recommended Practice / EV Charging Stations news — https://evchargingstations.com/chargingnews/sae-released-its-j3400-nacs-recommended-practice-document")
add("chaoji", "ChaoJi charging interface", "超级充电接口 ChaoJi", "charging",
    "Next-generation unified DC interface developed by China and Japan from the CHAdeMO 3.0 lineage, targeting 900 kW and above with backward compatibility through adapters.",
    "Driivz, EV charging standards and protocols — https://driivz.com/blog/ev-charging-standards-and-protocols")
add("iec-62196-type-2", "IEC 62196 Type 2 (Mennekes)", "IEC 62196 Type 2 交流接口", "charging",
    "Seven-pin AC connector used across Europe, supporting single- and three-phase charging up to 43.5 kW.",
    "PowerON EVSE, CCS1/CCS2/CHAdeMO/GB-T comparison — https://poweron-evse.com/ev-charging-insights/powering-the-future-a-deep-dive-into-ccs1-ccs2-chademo-and-gb-t-ev-charging-standards")
add("sae-j1772", "SAE J1772", "北美交流充电接口 SAE J1772", "charging",
    "North American AC charging connector and standard, rated up to 19.2 kW and also the AC half of CCS1.",
    "PowerON EVSE, CCS1/CCS2/CHAdeMO/GB-T comparison — https://poweron-evse.com/ev-charging-insights/powering-the-future-a-deep-dive-into-ccs1-ccs2-chademo-and-gb-t-ev-charging-standards")
add("iec-61851", "IEC 61851", "IEC 61851 传导充电系统标准", "charging",
    "International standard for conductive charging systems, defining charging modes 1 to 4 and the control pilot signalling used by AC charging.",
    "Wikipedia, GB/T charging standard (standards mapping) — https://en.wikipedia.org/wiki/GB/T_charging_standard")
add("iso-15118", "ISO 15118", "ISO 15118 车桩通信标准", "charging",
    "International vehicle-to-charger communication standard covering Plug and Charge via certificates; part 15118-20 adds bidirectional power transfer for V2G and V2H.",
    "Virta, Vehicle-to-Grid (V2G) explained — https://www.virta.global/vehicle-to-grid-v2g")
add("ocpp", "Open Charge Point Protocol (OCPP)", "开放充电桩通信协议", "charging",
    "Open protocol between charging stations and back-end management systems published by the Open Charge Alliance; it is independent of the vehicle-side plug standard.",
    "Open Charge Alliance / Driivz, EV charging standards and protocols — https://driivz.com/blog/ev-charging-standards-and-protocols")
add("plug-and-charge", "Plug and Charge", "即插即充", "charging",
    "Automatic authentication and billing at the start of a charging session using ISO 15118 certificate exchange, so no app or card is needed.",
    "ISO 15118 / Virta, V2G explained — https://www.virta.global/vehicle-to-grid-v2g")
add("ac-level-1", "AC Level 1 charging", "交流一级充电", "charging",
    "Charging from a standard household outlet at around 120 V in North America, giving roughly 1.4-1.9 kW.",
    "US DOE Alternative Fuels Data Center, charging levels — https://afdc.energy.gov/fuels/electricity_charging_home.html")
add("ac-level-2", "AC Level 2 charging", "交流二级充电", "charging",
    "208-240 V AC charging through a dedicated wallbox, typically 7-22 kW, corresponding to IEC 61851 mode 3.",
    "US DOE Alternative Fuels Data Center, charging levels — https://afdc.energy.gov/fuels/electricity_charging_home.html")
add("ac-11kw", "11 kW AC charging", "11 千瓦交流充电", "charging",
    "Three-phase AC charging at 16 A per phase; the common European default onboard charger rating.",
    "US DOE Alternative Fuels Data Center, charging levels — https://afdc.energy.gov/fuels/electricity_charging_home.html")
add("ac-22kw", "22 kW AC charging", "22 千瓦交流充电", "charging",
    "Three-phase AC charging at 32 A per phase; it requires a matching onboard charger and is limited by vehicle hardware, not the wallbox.",
    "US DOE Alternative Fuels Data Center, charging levels — https://afdc.energy.gov/fuels/electricity_charging_home.html")
add("dc-fast-charging", "DC fast charging (DCFC)", "直流快充", "charging",
    "Charging in which the off-board charger supplies DC directly to the pack, bypassing the onboard charger; typical public rates run from 50 kW to 400 kW and above.",
    "US DOE Alternative Fuels Data Center, charging levels — https://afdc.energy.gov/fuels/electricity_charging_home.html")
add("high-power-charging-350kw", "High-power charging (HPC, 350 kW+)", "大功率充电 (HPC)", "charging",
    "CCS2-class public chargers rated 350-400 kW, used with 800 V vehicles to add roughly 250-300 km in about 15-20 minutes.",
    "Ionity / Driivz, EV charging standards and protocols — https://driivz.com/blog/ev-charging-standards-and-protocols")
add("400v-architecture", "400 V architecture", "400V 电压平台", "charging",
    "Conventional EV pack and drivetrain voltage class around 350-450 V; DC charging current must rise steeply to exceed roughly 150-200 kW.",
    "PowerON EVSE / industry 800V platform overviews — https://poweron-evse.com/ev-charging-insights/powering-the-future-a-deep-dive-into-ccs1-ccs2-chademo-and-gb-t-ev-charging-standards",
    ["byd-atto-3", "aion-y", "leapmotor-c11"])
add("800v-architecture", "800 V high-voltage architecture", "800V 高压平台", "charging",
    "Doubling system voltage halves current for the same power, cutting cable and inverter losses and enabling sustained 250 kW+ charging with silicon carbide semiconductors.",
    "PowerON EVSE / industry 800V platform overviews — https://poweron-evse.com/ev-charging-insights/powering-the-future-a-deep-dive-into-ccs1-ccs2-chademo-and-gb-t-ev-charging-standards",
    ["zeekr-001", "xiaomi-su7", "nio-et7", "zeekr-009", "xpeng-g9"])
add("4c-fast-charging", "4C fast charging", "4C 快充", "charging",
    "Charging at four times pack capacity, which corresponds to a full charge in about 15 minutes and requires a dedicated high-rate battery design.",
    CATL_STD,
    ["zeekr-001", "xiaomi-su7"])
add("5c-fast-charging", "5C fast charging", "5C 超充", "charging",
    "Charging at five times pack capacity; on a 5C-capable pack this yields roughly 10-80% in about ten minutes when paired with a high-power charger.",
    CATL_STD,
    ["zeekr-001", "byd-han-l"])
add("megawatt-charging-system", "Megawatt Charging System (MCS)", "兆瓦级充电系统 (MCS)", "charging",
    "CharIN standard for heavy-duty vehicle charging targeting up to 3.75 MW at 1,250 V and 3,000 A.",
    "CharIN, Megawatt Charging System — https://www.charin.global/technology/mcs/")
add("battery-swapping", "Battery swapping", "换电", "charging",
    "Replenishment model in which the depleted pack is removed and a charged one installed, taking a few minutes and decoupling charging time from the vehicle.",
    "Wikipedia, Battery swapping — https://en.wikipedia.org/wiki/Battery_swapping",
    ["nio-es6", "nio-et5", "nio-et7"])
add("nio-power-swap", "NIO Power Swap", "蔚来换电", "charging",
    "NIO's automated battery swap stations, offered together with Battery-as-a-Service so customers lease the pack separately from the car.",
    "NIO official, Battery as a Service — https://www.nio.com/",
    ["nio-es6", "nio-et5", "nio-et7", "nio-es8"])
add("v2g", "Vehicle-to-grid (V2G)", "车网互动 (V2G)", "charging",
    "Exporting energy from an EV battery back to the public grid in exchange for payment; it requires a bidirectional vehicle, a bidirectional charger and a utility programme.",
    "Virta, Vehicle-to-Grid (V2G) explained — https://www.virta.global/vehicle-to-grid-v2g",
    ["nio-et7", "zeekr-009"])
add("v2l", "Vehicle-to-load (V2L)", "对外放电 (V2L)", "charging",
    "Powering external appliances from the traction battery through an outlet or adaptor, typically at 3.6 kW in Europe and up to 6 kW on some Chinese models.",
    "Mobility House, Which cars are V2G capable — https://mobilityhouse-energy.com/int_en/knowledge-center/article/which-cars-are-v2g-capable",
    ["byd-atto-3", "zeekr-001", "nio-et7"])
add("v2h", "Vehicle-to-home (V2H)", "车家互联 (V2H)", "charging",
    "Using the EV battery as a home backup or peak-shaving source through a bidirectional home charger.",
    "Mobility House, Which cars are V2G capable — https://mobilityhouse-energy.com/int_en/knowledge-center/article/which-cars-are-v2g-capable")
add("bidirectional-charging", "Bidirectional charging", "双向充电", "charging",
    "Hardware and software that allow power to flow both into and out of the vehicle battery, enabling V2L, V2H and V2G use cases.",
    "Virta, Vehicle-to-Grid (V2G) explained — https://www.virta.global/vehicle-to-grid-v2g")
add("charging-curve", "Charging curve", "充电曲线", "charging",
    "Plot of charging power against state of charge. Power is highest at low SOC and tapers above roughly 80%, so the last 20% takes disproportionately long.",
    "Driivz, EV charging standards and protocols — https://driivz.com/blog/ev-charging-standards-and-protocols")
add("onboard-charger", "Onboard charger (OBC)", "车载充电机 (OBC)", "charging",
    "AC-to-DC converter built into the vehicle that sets the maximum AC charging rate, commonly 6.6-11 kW and up to 22 kW on three-phase models.",
    "US DOE Alternative Fuels Data Center, charging levels — https://afdc.energy.gov/fuels/electricity_charging_home.html")
add("tesla-supercharger", "Tesla Supercharger", "特斯拉超级充电站", "charging",
    "Tesla's proprietary DC fast charging network; V3 cabinets deliver 250 kW and V4 cabinets up to 500 kW with 1,000 V support.",
    "Tesla official, Supercharging — https://www.tesla.com/supercharger")

# -------------------------------------------------------------- drivetrain (23)
add("pmsm", "Permanent magnet synchronous motor (PMSM)", "永磁同步电机", "drivetrain",
    "AC motor whose rotor uses permanent magnets, giving high power density and efficiency; the dominant traction motor in Chinese EVs.",
    "Wikipedia, Permanent magnet synchronous motor — https://en.wikipedia.org/wiki/Permanent_magnet_synchronous_motor",
    ["byd-seal", "aion-y", "xpeng-g9", "leapmotor-c11"])
add("induction-motor", "AC induction motor", "交流异步(感应)电机", "drivetrain",
    "Motor that induces rotor current instead of using permanent magnets; it is robust and can be freewheeled to cut drag when not needed.",
    "Wikipedia, Induction motor — https://en.wikipedia.org/wiki/Induction_motor")
add("wound-rotor-synchronous-motor", "Wound-rotor synchronous motor (EESM)", "电励磁同步电机 (EESM)", "drivetrain",
    "Synchronous motor that creates the rotor field with a wound coil instead of permanent magnets, eliminating rare-earth materials at a small efficiency cost.",
    "ZF, I2SM electric motor / BMW 5th-generation eDrive — https://www.zf.com/")
add("switched-reluctance-motor", "Switched reluctance motor", "开关磁阻电机", "drivetrain",
    "Motor that produces torque purely from magnetic reluctance, with a simple iron rotor that needs no magnets or windings but requires advanced control to limit noise.",
    "Wikipedia, Switched reluctance motor — https://en.wikipedia.org/wiki/Switched_reluctance_motor")
add("e-axle", "e-axle (integrated electric drive unit)", "电驱动桥 (e-axle)", "drivetrain",
    "Single assembly combining traction motor, inverter and reduction gearbox on one axle, which shortens high-voltage cabling and cuts weight and cost.",
    "Wikipedia, Electric vehicle (powertrain) — https://en.wikipedia.org/wiki/Electric_vehicle")
add("sic-power-module", "Silicon carbide (SiC) power module", "碳化硅功率模块", "drivetrain",
    "Wide-bandgap semiconductor used in inverters; it switches faster and tolerates higher temperatures than silicon, raising efficiency and enabling higher switching frequency.",
    "Wikipedia, Silicon carbide (power electronics) — https://en.wikipedia.org/wiki/Silicon_carbide")
add("igbt", "Insulated-gate bipolar transistor (IGBT)", "绝缘栅双极型晶体管 (IGBT)", "drivetrain",
    "Silicon power switch used in traction inverters and onboard chargers, combining high input impedance with low conduction loss at moderate switching frequency.",
    "Wikipedia, Insulated-gate bipolar transistor — https://en.wikipedia.org/wiki/Insulated-gate_bipolar_transistor")
add("dual-motor-awd", "Dual-motor all-wheel drive", "双电机四驱", "drivetrain",
    "Configuration with one motor per axle, giving all-wheel traction and independent front/rear torque split without a mechanical propshaft.",
    "Wikipedia, Electric vehicle (powertrain) — https://en.wikipedia.org/wiki/Electric_vehicle",
    ["zeekr-001", "nio-et7", "xpeng-g9"])
add("tri-motor", "Tri-motor drivetrain", "三电机驱动", "drivetrain",
    "Three-motor layout, usually one front and two rear, used for high-performance models with rear torque vectoring.",
    "Wikipedia, Tesla Model S (Plaid tri-motor) — https://en.wikipedia.org/wiki/Tesla_Model_S")
add("quad-motor", "Quad-motor drivetrain", "四电机驱动", "drivetrain",
    "Four independent motors, one per wheel, enabling precise wheel-level torque control for off-road capability such as tank turns.",
    "Wikipedia, Yangwang U8 / BYD e4 platform — https://en.wikipedia.org/wiki/Yangwang_U8")
add("single-speed-reducer", "Single-speed reduction gear", "单速减速器", "drivetrain",
    "Fixed-ratio gearbox between motor and wheels used by most EVs, because the motor's wide speed range removes the need for multiple ratios.",
    "Wikipedia, Electric vehicle (transmission) — https://en.wikipedia.org/wiki/Electric_vehicle")
add("two-speed-transmission", "Two-speed transmission", "两挡变速器", "drivetrain",
    "Two-ratio gearbox used in some performance EVs so a short first gear improves launch and a long second gear raises top-speed efficiency.",
    "Wikipedia, Porsche Taycan — https://en.wikipedia.org/wiki/Porsche_Taycan")
add("regenerative-braking", "Regenerative braking", "再生制动", "drivetrain",
    "Recovering kinetic energy by running the traction motor as a generator during deceleration and storing the energy back in the battery.",
    "Wikipedia, Regenerative brake — https://en.wikipedia.org/wiki/Regenerative_brake")
add("one-pedal-driving", "One-pedal driving", "单踏板模式", "drivetrain",
    "Driving mode in which strong regenerative braking is mapped to the accelerator pedal, so the brake pedal is rarely needed in normal traffic.",
    "Wikipedia, Regenerative brake — https://en.wikipedia.org/wiki/Regenerative_brake")
add("torque-vectoring", "Torque vectoring", "扭矩矢量控制", "drivetrain",
    "Deliberately distributing drive torque left to right to rotate the car into a corner, which multi-motor EVs can do without a differential.",
    "Wikipedia, Torque vectoring — https://en.wikipedia.org/wiki/Torque_vectoring",
    ["zeekr-001"])
add("in-wheel-motor", "In-wheel motor", "轮毂电机", "drivetrain",
    "Motor mounted inside the wheel hub, removing the drivetrain entirely but raising unsprung mass; used mainly in low-speed and specialist vehicles.",
    "Wikipedia, Wheel hub motor — https://en.wikipedia.org/wiki/Wheel_hub_motor")
add("rare-earth-free-motor", "Rare-earth-free motor", "无稀土电机", "drivetrain",
    "Traction motor designed without neodymium or dysprosium magnets, using wound-field or ferrite designs to avoid rare-earth supply risk.",
    "ZF, I2SM electric motor (rare-earth-free) — https://www.zf.com/")
add("dm-i-super-hybrid", "BYD DM-i super hybrid", "比亚迪 DM-i 超级混动", "drivetrain",
    "Plug-in hybrid system built around an electric hybrid architecture in which the engine mainly generates electricity, with a dedicated hybrid transmission for direct drive at high speed.",
    "BYD official, DM-i super hybrid — https://www.byd.com/",
    ["byd-qin-plus-dm-i", "byd-song-plus-dm-i", "byd-han-dm-i"])
add("erev-range-extender", "Range-extender EV (EREV)", "增程式电动车 (EREV)", "drivetrain",
    "Series hybrid in which the combustion engine only drives a generator, so the wheels are always driven electrically; battery packs are typically larger than in a PHEV.",
    "Wikipedia, Range extender (vehicle) — https://en.wikipedia.org/wiki/Range_extender_(vehicle)",
    ["li-auto-l9", "aito-m9", "deepal-s07-erev", "leapmotor-c11-erev"])
add("phev", "Plug-in hybrid (PHEV)", "插电式混合动力 (PHEV)", "drivetrain",
    "Vehicle with both a combustion engine and a chargeable battery that can drive the wheels directly or electrically; Chinese policy treats long-range PHEVs as new-energy vehicles.",
    "Wikipedia, Plug-in hybrid — https://en.wikipedia.org/wiki/Plug-in_hybrid")
add("dedicated-ev-platform", "Dedicated EV platform", "纯电专属平台", "drivetrain",
    "Vehicle architecture designed around a skateboard battery floor from the outset, rather than adapted from a combustion platform, giving a flat floor and more interior space.",
    "Wikipedia, Electric vehicle platform — https://en.wikipedia.org/wiki/Electric_vehicle")
add("battery-electric-vehicle", "Battery electric vehicle (BEV)", "纯电动车 (BEV)", "drivetrain",
    "Vehicle propelled solely by an electric motor drawing energy from an onboard battery, with no combustion engine.",
    "Wikipedia, Battery electric vehicle — https://en.wikipedia.org/wiki/Battery_electric_vehicle",
    ["byd-seal", "aion-y", "geely-galaxy-e5"])
add("power-density-motor", "Motor power density", "电机功率密度", "drivetrain",
    "Traction motor output per unit mass or volume, reported in kW/kg; higher values reduce drive-unit weight for a given output.",
    "Wikipedia, Power density — https://en.wikipedia.org/wiki/Power_density")

# ----------------------------------------------------------------- thermal (13)
add("liquid-cooling", "Liquid cooling (battery)", "电池液冷", "thermal",
    "Battery thermal management approach that circulates coolant through cold plates or channels to remove heat and equalise cell temperatures.",
    "Frontiers in Mechanical Engineering, CTB review (thermal management) — https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1825484/full")
add("direct-cooling-refrigerant", "Direct refrigerant cooling", "电池直冷", "thermal",
    "Design that routes refrigerant directly to a cold plate on the pack, removing the intermediate coolant loop for faster heat rejection.",
    "Frontiers in Mechanical Engineering, CTB review (thermal management) — https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1825484/full")
add("immersion-cooling", "Immersion cooling", "浸没式冷却", "thermal",
    "Cooling in which cells are submerged in a dielectric fluid, giving very uniform temperature control and suppressing thermal propagation.",
    "Wikipedia, Immersion cooling — https://en.wikipedia.org/wiki/Immersion_cooling")
add("heat-pump-hvac", "Heat pump HVAC", "热泵空调", "thermal",
    "Cabin heating system that moves heat with a refrigerant cycle instead of generating it resistively, saving substantial energy in cold weather.",
    "US DOE, Heat pumps for EV cabin heating / Wikipedia, Heat pump — https://en.wikipedia.org/wiki/Heat_pump",
    ["byd-atto-3", "zeekr-001"])
add("co2-heat-pump", "CO2 (R744) heat pump", "二氧化碳热泵 (R744)", "thermal",
    "Heat pump using carbon dioxide as refrigerant; it keeps useful heating capacity at very low ambient temperature and has very low global warming potential.",
    "Wikipedia, R744 (CO2 refrigerant) — https://en.wikipedia.org/wiki/Carbon_dioxide#Refrigerant")
add("ptc-heater", "PTC heater", "PTC 加热器", "thermal",
    "Positive-temperature-coefficient resistive heater used for cabin and battery heating; simple and effective but consumes significant energy.",
    "Wikipedia, Positive temperature coefficient heater — https://en.wikipedia.org/wiki/Positive_temperature_coefficient")
add("battery-preconditioning", "Battery preconditioning", "电池预热/预冷", "thermal",
    "Automatically bringing the pack to an optimal temperature before fast charging; cold packs otherwise charge far more slowly.",
    "US DOE / industry fast-charging guidance — https://afdc.energy.gov/fuels/electricity_charging_home.html")
add("battery-thermal-management-system", "Battery thermal management system (BTMS)", "电池热管理系统 (BTMS)", "thermal",
    "Combined hardware and control strategy that keeps cells within a target temperature window, balancing cooling, heating and temperature uniformity.",
    "Frontiers in Mechanical Engineering, CTB review — https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1825484/full")
add("octovalve", "Octovalve thermal manifold", "八通阀热管理集成模块", "thermal",
    "Multi-port valve that routes coolant between battery, drive units, cabin and heat pump from a single manifold, cutting the number of thermal loops and valves.",
    "Tesla, Model Y heat pump / Octovalve patent coverage — https://www.tesla.com/")
add("phase-change-material", "Phase change material (PCM)", "相变材料 (PCM)", "thermal",
    "Material that absorbs heat while melting at a set temperature, used to buffer cell temperature spikes and slow thermal propagation.",
    "Wikipedia, Phase-change material — https://en.wikipedia.org/wiki/Phase-change_material")
add("motor-oil-cooling", "Motor oil cooling", "电机油冷", "thermal",
    "Spraying or circulating oil directly onto motor windings to remove heat; it raises continuous power density compared with water-jacket cooling.",
    "Wikipedia, Electric motor cooling / industry e-axle specifications — https://en.wikipedia.org/wiki/Electric_motor")
add("thermal-propagation-prevention", "Thermal runaway propagation prevention", "热失控扩散防护", "thermal",
    "Pack-level design measures such as barriers, venting and spacing that stop one cell's thermal runaway from igniting its neighbours; China's GB 38031-2025 makes no-fire, no-explosion thermal propagation a mandatory requirement.",
    "Xinhua / China MIIT, GB 38031-2025 (thermal diffusion test) — https://www.news.cn/20260629/2a2fa1facc034e6ea24b73bcd582ab43/c.html")
add("refrigerant-r1234yf", "R1234yf refrigerant", "制冷剂 R1234yf", "thermal",
    "Low global-warming-potential HFO refrigerant that replaced R134a in most automotive air-conditioning systems.",
    "Wikipedia, 2,3,3,3-Tetrafluoropropene (R-1234yf) — https://en.wikipedia.org/wiki/2,3,3,3-Tetrafluoropropene")

# ------------------------------------------------------------------- range (11)
add("cltc", "CLTC range standard", "中国 CLTC 续航工况", "range",
    "China Light-Duty Vehicle Test Cycle defined in GB/T 38146.1-2019: a 30-minute, 14.48 km dynamometer cycle with low average speed and frequent stops, which usually reads more optimistic than real-world driving.",
    "Wikipedia, China Light-Duty Vehicle Test Cycle — https://en.wikipedia.org/wiki/China_Light-Duty_Vehicle_Test_Cycle")
add("wltp", "WLTP range standard", "WLTP 全球统一测试规程", "range",
    "Worldwide Harmonised Light Vehicles Test Procedure, the lab cycle that replaced NEDC in Europe; its four-phase speed profile sits closer to real driving than NEDC.",
    "Wikipedia, Worldwide Harmonised Light Vehicles Test Procedure — https://en.wikipedia.org/wiki/Worldwide_Harmonised_Light_Vehicles_Test_Procedure")
add("nedc", "NEDC range standard", "NEDC 新欧洲行驶工况", "range",
    "New European Driving Cycle, a synthetic two-phase laboratory cycle replaced by WLTP in Europe from 2017-2019; its stable speed profile made range figures optimistic.",
    "Wikipedia, New European Driving Cycle — https://en.wikipedia.org/wiki/New_European_Driving_Cycle")
add("epa-range", "EPA range rating", "美国 EPA 续航", "range",
    "United States EPA rating derived from the UDDS urban and HWFET highway cycles with a 0.7 adjustment factor, making it the most conservative of the major range claims.",
    "US EPA / FuelEconomy.gov — https://www.fueleconomy.gov/feg/evtech.shtml")
add("range-standard-conversion", "Range standard conversion", "续航口径换算", "range",
    "Rules of thumb for translating one test cycle into another, such as CLTC multiplied by about 0.82 to approximate WLTP; they are estimates and should always carry the source standard.",
    "Wikipedia, China Light-Duty Vehicle Test Cycle (cycle comparison table) — https://en.wikipedia.org/wiki/China_Light-Duty_Vehicle_Test_Cycle")
add("real-world-range", "Real-world range", "真实续航", "range",
    "Distance actually achieved on the road, typically below every laboratory figure because of speed, gradient, load, climate control and temperature.",
    "Wikipedia, China Light-Duty Vehicle Test Cycle (cycle comparison) — https://en.wikipedia.org/wiki/China_Light-Duty_Vehicle_Test_Cycle")
add("winter-range-retention", "Winter range retention", "冬季续航保持率", "range",
    "Share of rated range available in sub-zero conditions; cabin heating and cold cell chemistry cut it sharply, and LFP packs lose more than NMC.",
    "Wikipedia, Electric vehicle (cold weather) — https://en.wikipedia.org/wiki/Electric_vehicle")
add("energy-consumption", "Energy consumption (kWh/100 km)", "百公里电耗", "range",
    "Energy used per 100 km, the metric that links battery size to range and the fairest basis for comparing efficiency between models.",
    "Wikipedia, China Light-Duty Vehicle Test Cycle (consumption comparison) — https://en.wikipedia.org/wiki/China_Light-Duty_Vehicle_Test_Cycle")
add("range-anxiety", "Range anxiety", "续航焦虑", "range",
    "Consumer concern about running out of charge before reaching a charger, a barrier to EV adoption that charger coverage and faster charging reduce.",
    "Wikipedia, Range anxiety — https://en.wikipedia.org/wiki/Range_anxiety")
add("usable-vs-gross-capacity", "Usable versus gross battery capacity", "电池可用容量与标称容量", "range",
    "Difference between total installed capacity and the portion the BMS exposes to the driver; buffers protect the pack and mean some kWh are never usable.",
    "Wikipedia, Electric vehicle battery — https://en.wikipedia.org/wiki/Electric_vehicle_battery")
add("highway-range-penalty", "Highway range penalty", "高速续航衰减", "range",
    "Additional energy per kilometre at steady high speed because aerodynamic drag grows with the square of velocity; low-speed cycles such as CLTC under-represent this effect.",
    "Wikipedia, Drag (physics) / Automotive aerodynamics — https://en.wikipedia.org/wiki/Automotive_aerodynamics")

# ------------------------------------------------------------- body-safety (15)
add("gigacasting", "Integrated die-casting (gigacasting)", "一体化压铸", "body-safety",
    "Casting large body sections such as a rear underbody as a single part using very high clamping-force presses, replacing dozens of welded stampings.",
    "Wikipedia, Tesla (manufacturing) / Giga Press — https://en.wikipedia.org/wiki/Giga_Press")
add("drag-coefficient", "Drag coefficient (Cd)", "风阻系数", "body-safety",
    "Dimensionless measure of how much aerodynamic drag a shape creates; combined with frontal area it defines CdA, which dominates highway energy use.",
    "Wikipedia, Automobile drag coefficient — https://en.wikipedia.org/wiki/Automobile_drag_coefficient")
add("active-grille-shutter", "Active grille shutter", "主动进气格栅", "body-safety",
    "Grille vanes that close at speed to cut cooling airflow drag and reopen when the drive system needs cooling.",
    "Wikipedia, Automobile drag coefficient — https://en.wikipedia.org/wiki/Automobile_drag_coefficient")
add("flush-door-handle", "Flush door handle", "隐藏式门把手", "body-safety",
    "Handle that stows flush with the door skin, removing a local separation bubble and reducing drag.",
    "Wikipedia, Automobile drag coefficient — https://en.wikipedia.org/wiki/Automobile_drag_coefficient")
add("flat-underbody", "Flat underbody panel", "平整底盘护板", "body-safety",
    "Smooth panelling under the car that prevents turbulent airflow underneath the battery, lowering drag and adding protection to the pack.",
    "Wikipedia, Automobile drag coefficient — https://en.wikipedia.org/wiki/Automobile_drag_coefficient")
add("air-suspension", "Air suspension", "空气悬架", "body-safety",
    "Springing that uses air springs with adjustable pressure and height, letting the car lower itself at speed for aerodynamic benefit or raise itself over rough ground.",
    "Wikipedia, Air suspension — https://en.wikipedia.org/wiki/Air_suspension")
add("crumple-zone", "Crumple zone", "溃缩吸能区", "body-safety",
    "Deliberately deformable front or rear structure that absorbs crash energy over a controlled distance so the passenger cell stays intact.",
    "Wikipedia, Crumple zone — https://en.wikipedia.org/wiki/Crumple_zone")
add("hot-stamped-steel", "Hot-stamped ultra-high-strength steel", "热成型超高强钢", "body-safety",
    "Steel press-formed while austenitic and quenched in the die, reaching tensile strengths around 1,500 MPa for lightweight passenger-cell reinforcement.",
    "Wikipedia, Hot stamping — https://en.wikipedia.org/wiki/Hot_stamping")
add("aluminium-space-frame", "Aluminium space frame", "全铝车身框架", "body-safety",
    "Body structure built from extruded and bonded aluminium sections rather than a monocoque of steel stampings, cutting weight at higher material cost.",
    "Wikipedia, Space frame — https://en.wikipedia.org/wiki/Space_frame")
add("torsional-stiffness", "Torsional stiffness", "车身扭转刚度", "body-safety",
    "Resistance of the body to twisting, measured in Nm/deg; structural battery designs such as CTB push values above 40,000 Nm/deg.",
    "ResearchInChina, Passenger Car CTP/CTC/CTB report (CTB structural contribution) — https://www.researchinchina.com/Htmls/Report/2024/73951.html")
add("ip68-battery-pack", "IP68 battery pack sealing", "电池包 IP68 防护", "body-safety",
    "Pack sealing rated dust-tight and protected against continuous immersion, the common rating for EV traction batteries.",
    "Wikipedia, IP code — https://en.wikipedia.org/wiki/IP_code")
add("ip-rating", "IP code", "防护等级 (IP 代码)", "body-safety",
    "International two-digit ingress protection rating: the first digit covers solids and dust, the second covers water.",
    "Wikipedia, IP code — https://en.wikipedia.org/wiki/IP_code")
add("c-ncap", "C-NCAP", "中国新车评价规程 C-NCAP", "body-safety",
    "Chinese new car assessment programme run by CATARC that scores crash protection and, in recent versions, active safety and battery safety for the domestic market.",
    "C-NCAP official / CATARC — https://www.c-ncap.org.cn/")
add("euro-ncap", "Euro NCAP", "欧洲新车安全评鉴 Euro NCAP", "body-safety",
    "European new car assessment programme scoring adult and child occupant protection, vulnerable road user protection and safety assist systems.",
    "Euro NCAP official — https://www.euroncap.com/")
add("gb-38031", "GB 38031 EV battery safety standard", "动力电池安全强制性国标 GB 38031", "body-safety",
    "China's mandatory safety standard for traction batteries. The 2020 version required a five-minute warning before fire or explosion; the 2025 revision, published in March 2025, demands no fire and no explosion plus smoke that does not harm occupants, and adds bottom-impact and post-fast-charge short-circuit tests. It applies to newly type-approved models from 1 July 2026 and to already-approved models from 1 July 2027.",
    "China MIIT / Xinhua, GB 38031-2025 Electric vehicles traction battery safety requirements — https://www.news.cn/20260629/2a2fa1facc034e6ea24b73bcd582ab43/c.html")

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "data", "technical-master.json")

ids = [e["id"] for e in E]
dup = {i for i in ids if ids.count(i) > 1}
if dup:
    sys.exit("duplicate ids: %s" % dup)
cats = {}
for e in E:
    cats[e["category"]] = cats.get(e["category"], 0) + 1
for e in E:
    assert e["id"] and e["name"] and e["category"] and e["definition"] and e["source"], e
    assert e["definition"].strip().endswith("."), e["id"]

doc = {"generated": "2026-09-15", "count": len(E), "entities": E}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("wrote", OUT)
print("count:", len(E))
print("categories:", cats)
