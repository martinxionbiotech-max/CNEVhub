# EV Hub Indexation Quality Gate

> 生成：2026-09-17 ｜ 车辆总数：517 ｜ 工具：scripts/quality-gate.mjs（`npm run quality:gate`）
> 本报告仅产出不完整清单，**不自动 noindex**（无既有政策支持）。

## 五门槛通过率

| Gate | 通过 | 未通过 | 说明 |
|---|---|---|---|
| identity | 517 | 0 | vehicle_id/model/slug/title/publishedDate 完整 |
| brand | 517 | 0 | brand 在 brand-master 且品牌页存在 |
| powertrain | 516 | 1 | 受控词表内且非 Unknown |
| specs | 444 | 73 | price/range/battery/body_type/motor_power 有效 |
| source | 517 | 0 | master source/source_url + md data_source 存在 |

## 不完整记录清单（73 台）

- [aeolus-huge](https://electricvehiclehub.net/vehicles/aeolus-huge/) (aeolus)
  - specs: range 全空
- [aeolus-mage](https://electricvehiclehub.net/vehicles/aeolus-mage/) (aeolus)
  - specs: range 全空; battery_kwh 空
- [changan-cs75](https://electricvehiclehub.net/vehicles/changan-cs75/) (changan)
  - specs: range 全空; battery_kwh 空
- [changan-nevo-lamore](https://electricvehiclehub.net/vehicles/changan-nevo-lamore/) (changan)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [changan-x5-plus](https://electricvehiclehub.net/vehicles/changan-x5-plus/) (changan)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [gac-motor-emkoo](https://electricvehiclehub.net/vehicles/gac-motor-emkoo/) (gac-motor)
  - specs: range 全空; battery_kwh 空
- [gac-motor-empow](https://electricvehiclehub.net/vehicles/gac-motor-empow/) (gac-motor)
  - specs: range 全空
- [gac-motor-gs8](https://electricvehiclehub.net/vehicles/gac-motor-gs8/) (gac-motor)
  - specs: range 全空; battery_kwh 空
- [geely-galaxy-xingrui-l](https://electricvehiclehub.net/vehicles/geely-galaxy-xingrui-l/) (geely-galaxy)
  - specs: range 全空; battery_kwh 空
- [haval-jolion-pro](https://electricvehiclehub.net/vehicles/haval-jolion-pro/) (haval)
  - specs: range 全空; battery_kwh 空
- [haval-shenshou](https://electricvehiclehub.net/vehicles/haval-shenshou/) (haval)
  - specs: range 全空
- [hongqi-guoya](https://electricvehiclehub.net/vehicles/hongqi-guoya/) (hongqi)
  - powertrain: Unknown（无法索引分类）
  - specs: range 全空; battery_kwh 空
- [wuling-asta](https://electricvehiclehub.net/vehicles/wuling-asta/) (wuling)
  - specs: range 全空; battery_kwh 空
- [wuling-jiachen](https://electricvehiclehub.net/vehicles/wuling-jiachen/) (wuling)
  - specs: range 全空; battery_kwh 空
- [wuling-nebula](https://electricvehiclehub.net/vehicles/wuling-nebula/) (wuling)
  - specs: range 全空; battery_kwh 空
- [wuling-victory](https://electricvehiclehub.net/vehicles/wuling-victory/) (wuling)
  - specs: range 全空; battery_kwh 空
- [byd-qin-max-ev](https://electricvehiclehub.net/vehicles/byd-qin-max-ev/) (byd)
  - specs: range 全空; battery_kwh 空
- [byd-qin-max-dm-i](https://electricvehiclehub.net/vehicles/byd-qin-max-dm-i/) (byd)
  - specs: battery_kwh 空; motor_power_kw 空
- [geely-galaxy-starshine-7](https://electricvehiclehub.net/vehicles/geely-galaxy-starshine-7/) (geely-galaxy)
  - specs: battery_kwh 空; motor_power_kw 空
- [geely-galaxy-starship-7-ev](https://electricvehiclehub.net/vehicles/geely-galaxy-starship-7-ev/) (geely-galaxy)
  - specs: battery_kwh 空
- [chery-fulwin-a8l](https://electricvehiclehub.net/vehicles/chery-fulwin-a8l/) (chery-fulwin)
  - specs: motor_power_kw 空
- [chery-fulwin-t6](https://electricvehiclehub.net/vehicles/chery-fulwin-t6/) (chery-fulwin)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [chery-fulwin-t9l](https://electricvehiclehub.net/vehicles/chery-fulwin-t9l/) (chery-fulwin)
  - specs: battery_kwh 空
- [chery-fulwin-x3](https://electricvehiclehub.net/vehicles/chery-fulwin-x3/) (chery-fulwin)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [chery-fulwin-x3-plus](https://electricvehiclehub.net/vehicles/chery-fulwin-x3-plus/) (chery-fulwin)
  - specs: battery_kwh 空; motor_power_kw 空
- [chery-new-energy-qq3](https://electricvehiclehub.net/vehicles/chery-new-energy-qq3/) (chery-new-energy)
  - specs: battery_kwh 空
- [exeed-et5](https://electricvehiclehub.net/vehicles/exeed-et5/) (exeed)
  - specs: battery_kwh 空
- [jetour-shanhai-l9](https://electricvehiclehub.net/vehicles/jetour-shanhai-l9/) (jetour)
  - specs: motor_power_kw 空
- [icaur-03t](https://electricvehiclehub.net/vehicles/icaur-03t/) (icaur)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [changan-cs55-plus-hev](https://electricvehiclehub.net/vehicles/changan-cs55-plus-hev/) (changan)
  - specs: range 全空
- [changan-cs75-plus-hev](https://electricvehiclehub.net/vehicles/changan-cs75-plus-hev/) (changan)
  - specs: range 全空; battery_kwh 空
- [changan-eado-hev](https://electricvehiclehub.net/vehicles/changan-eado-hev/) (changan)
  - specs: range 全空; battery_kwh 空
- [changan-uni-v-hev](https://electricvehiclehub.net/vehicles/changan-uni-v-hev/) (changan)
  - specs: range 全空
- [xpeng-g9l](https://electricvehiclehub.net/vehicles/xpeng-g9l/) (xpeng)
  - specs: battery_kwh 空; motor_power_kw 空
- [xpeng-mona-l03](https://electricvehiclehub.net/vehicles/xpeng-mona-l03/) (xpeng)
  - specs: battery_kwh 空
- [leapmotor-d99](https://electricvehiclehub.net/vehicles/leapmotor-d99/) (leapmotor)
  - specs: motor_power_kw 空
- [xiaomi-skynomad-n90](https://electricvehiclehub.net/vehicles/xiaomi-skynomad-n90/) (xiaomi)
  - specs: motor_power_kw 空
- [aito-m6](https://electricvehiclehub.net/vehicles/aito-m6/) (aito)
  - specs: motor_power_kw 空
- [aito-m9-ultimate](https://electricvehiclehub.net/vehicles/aito-m9-ultimate/) (aito)
  - specs: battery_kwh 空; motor_power_kw 空
- [dongfeng-epi-m8](https://electricvehiclehub.net/vehicles/dongfeng-epi-m8/) (dongfeng-e)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [dongfeng-epi-007-plus](https://electricvehiclehub.net/vehicles/dongfeng-epi-007-plus/) (dongfeng-e)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [forthing-xinghai-v6-plus](https://electricvehiclehub.net/vehicles/forthing-xinghai-v6-plus/) (forthing)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [forthing-thunder](https://electricvehiclehub.net/vehicles/forthing-thunder/) (forthing)
  - specs: battery_kwh 空
- [voyah-passion-l](https://electricvehiclehub.net/vehicles/voyah-passion-l/) (voyah)
  - specs: motor_power_kw 空
- [hongqi-tiangong-06](https://electricvehiclehub.net/vehicles/hongqi-tiangong-06/) (hongqi)
  - specs: battery_kwh 空
- [haval-xiaolong-max](https://electricvehiclehub.net/vehicles/haval-xiaolong-max/) (haval)
  - specs: battery_kwh 空
- [ora-5](https://electricvehiclehub.net/vehicles/ora-5/) (ora)
  - specs: battery_kwh 空; motor_power_kw 空
- [jac-ieva50](https://electricvehiclehub.net/vehicles/jac-ieva50/) (jac)
  - specs: range 全空
- [jmc-yichi-ev3](https://electricvehiclehub.net/vehicles/jmc-yichi-ev3/) (jmc)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [jmc-yi-chi-05s](https://electricvehiclehub.net/vehicles/jmc-yi-chi-05s/) (jmc)
  - specs: battery_kwh 空; motor_power_kw 空
- [jmc-yi-chi-06](https://electricvehiclehub.net/vehicles/jmc-yi-chi-06/) (jmc)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [aion-v-plus](https://electricvehiclehub.net/vehicles/aion-v-plus/) (aion)
  - specs: range 全空; battery_kwh 空
- [hyptec-s600](https://electricvehiclehub.net/vehicles/hyptec-s600/) (hyptec)
  - specs: battery_kwh 空
- [gac-motor-xiangwang-s7](https://electricvehiclehub.net/vehicles/gac-motor-xiangwang-s7/) (gac-motor)
  - specs: motor_power_kw 空
- [gac-motor-xiangwang-m8](https://electricvehiclehub.net/vehicles/gac-motor-xiangwang-m8/) (gac-motor)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [roewe-r7](https://electricvehiclehub.net/vehicles/roewe-r7/) (roewe)
  - specs: range 全空
- [roewe-imax8-dmh](https://electricvehiclehub.net/vehicles/roewe-imax8-dmh/) (roewe)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [im-ls8](https://electricvehiclehub.net/vehicles/im-ls8/) (im)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [maxus-mifa-7-phev](https://electricvehiclehub.net/vehicles/maxus-mifa-7-phev/) (maxus)
  - specs: range 全空
- [maxus-mifa-9-phev](https://electricvehiclehub.net/vehicles/maxus-mifa-9-phev/) (maxus)
  - specs: range 全空; battery_kwh 空; motor_power_kw 空
- [wuling-starlight-560](https://electricvehiclehub.net/vehicles/wuling-starlight-560/) (wuling)
  - specs: motor_power_kw 空
- [geometry-e](https://electricvehiclehub.net/vehicles/geometry-e/) (geometry)
  - specs: range 全空
- [dayun-y7](https://electricvehiclehub.net/vehicles/dayun-y7/) (dayun)
  - specs: battery_kwh 空
- [cowin-kunlun-ihd](https://electricvehiclehub.net/vehicles/cowin-kunlun-ihd/) (cowin)
  - specs: range 全空; battery_kwh 空
- [seres-sf5](https://electricvehiclehub.net/vehicles/seres-sf5/) (seres)
  - specs: range 全空; motor_power_kw 空
- [landian-e5](https://electricvehiclehub.net/vehicles/landian-e5/) (landian)
  - specs: battery_kwh 空
- [jac-x8-ejia](https://electricvehiclehub.net/vehicles/jac-x8-ejia/) (jac)
  - specs: motor_power_kw 空
- [chery-tiggo-8-pro-new-energy](https://electricvehiclehub.net/vehicles/chery-tiggo-8-pro-new-energy/) (chery)
  - specs: battery_kwh 空
- [chery-explore-06-c-dm](https://electricvehiclehub.net/vehicles/chery-explore-06-c-dm/) (chery)
  - specs: motor_power_kw 空
- [kaicene-changxing-ev](https://electricvehiclehub.net/vehicles/kaicene-changxing-ev/) (kaicene)
  - specs: range 全空; battery_kwh 空
- [oshan-keshan-ev](https://electricvehiclehub.net/vehicles/oshan-keshan-ev/) (oshan)
  - specs: range 全空
- [mg-pilot-phev](https://electricvehiclehub.net/vehicles/mg-pilot-phev/) (mg)
  - specs: motor_power_kw 空
- [jac-ieva60](https://electricvehiclehub.net/vehicles/jac-ieva60/) (jac)
  - specs: motor_power_kw 空

## 建议（非阻塞）

- **specs**: range 全空的车辆建议补充 CLTC/WLTP 数据或标注 Unknown
- **powertrain**: Unknown powertrain 车辆标注需人工查证（如 Hongqi Guoya）
