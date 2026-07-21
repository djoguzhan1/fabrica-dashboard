import React, { useState } from "react";
import {
  Image,
  Pressable,
  SafeAreaView,
  StyleSheet,
  Text,
  TextInput,
  useWindowDimensions,
  View,
  ActivityIndicator,
} from "react-native";
import { StatusBar } from "expo-status-bar";
import Svg, { Defs, G, LinearGradient, Path, Rect, Stop } from "react-native-svg";

const BASE_WIDTH = 390;
const BACKGROUND = "#0A1428";
const INPUT_TEXT = "#E8FFF2";
const PLACEHOLDER = "rgba(232, 255, 242, 0.42)";
const BUTTON_TEXT = "#0D1A2A";
const ERROR_COLOR = "#FF6B6B";
const HOME_IMAGE_WIDTH = 1294;
const HOME_IMAGE_HEIGHT = 2800;
const HOME_BUTTON_AREAS = [
  { top: 21.0, left: 14.8, width: 74.5, height: 6.0 },
  { top: 36.0, left: 12.8, width: 76.5, height: 6.0 },
  { top: 51.3, left: 12.8, width: 76.5, height: 6.0 },
  { top: 68.0, left: 12.8, width: 76.5, height: 6.0 },
] as const;
const MACHINES_IMAGE_WIDTH = 390;
const MACHINES_IMAGE_HEIGHT = 844;
const MACHINE_LABELS = [
  { name: "MP550-001", left: 46.5, top: 135.0 },
  { name: "MP550-002", left: 250.0, top: 136.0 },
  { name: "MP550-003", left: 45.0, top: 370.0 },
  { name: "MP550-004", left: 250.0, top: 370.0 },
  { name: "MP550-005", left: 58.0, top: 585.0 },
  { name: "MP550-006", left: 260.0, top: 583.0 },
] as const;
const STATUS_LABELS = [
  { name: "MP550-001", left: 6.0, top: 285.0, label: "Cihaz Aktif", active: true },
  { name: "MP550-002", left: 218.0, top: 288.0, label: "Cihaz Aktif", active: true },
  { name: "MP550-003", left: 7.0, top: 513.0, label: "Cihaz Pasif", active: false },
  { name: "MP550-004", left: 223.0, top: 515.0, label: "Cihaz Pasif", active: false },
  { name: "MP550-005", left: 15.0, top: 726.0, label: "Cihaz Pasif", active: false },
  { name: "MP550-006", left: 223.0, top: 724.0, label: "Cihaz Pasif", active: false },
] as const;
const PLUG_ICONS = [
  { name: "MP550-001", left: 66.0, top: 266.0 },
  { name: "MP550-002", left: 276.0, top: 266.0 },
  { name: "MP550-003", left: 68.0, top: 491.0 },
  { name: "MP550-004", left: 276.0, top: 491.0 },
  { name: "MP550-005", left: 68.0, top: 716.0 },
  { name: "MP550-006", left: 276.0, top: 716.0 },
] as const;
const PLUG_PANEL_WIDTH = 54;
const PLUG_PANEL_HEIGHT = 34;
const PLUG_IMG_WIDTH = 54;
const PLUG_IMG_HEIGHT = 34;
const BADGE_IMG_WIDTH = 110;
const BADGE_IMG_HEIGHT = 24;
const HOME_DEBUG_HITBOX_COLOR = "transparent";
const DETAIL_SCREEN_WIDTH = 420;
const DETAIL_SCREEN_HEIGHT = 840;
const DETAIL_BACKGROUND = "#0B1E36";
const MACHINE_HITBOXES = [
  { left: 46.5, top: 135.0, width: 140, height: 150 },
  { left: 250.0, top: 136.0, width: 140, height: 150 },
  { left: 45.0, top: 370.0, width: 140, height: 150 },
  { left: 250.0, top: 370.0, width: 140, height: 150 },
  { left: 58.0, top: 585.0, width: 140, height: 150 },
  { left: 260.0, top: 583.0, width: 140, height: 150 },
] as const;

const ASSETS = {
  logo: require("./kırpılmıs_olanlar/MOSTRAVI-EXPORT.png"),
  emailInput: require("./kırpılmıs_olanlar/input_kutusu.png"),
  passwordInput: require("./kırpılmıs_olanlar/input_kutusu2.png"),
  button: require("./kırpılmıs_olanlar/giriş_yap_kutsu.png"),
  checkbox: require("./kırpılmıs_olanlar/kaydet_kutusu.png"),
  banner: require("./kırpılmıs_olanlar/alt.png"),
  detailBackArrow: require("./ic_back_arrow.png"),
  detailArrowLeft: require("./4. ekran/arrow_left.png"),
  detailArrowRight: require("./4. ekran/arrow_right.png"),
  detailStatusActive: require("./4. ekran/status_active.png"),
  detailProductionQty: require("./4. ekran/btn_uretim_adet.png"),
  detailProductionTimes: require("./4. ekran/btn_uretim_sureleri.png"),
  detailEfficiency: require("./4. ekran/btn_verimlilik.png"),
  detailScrapQty: require("./4. ekran/btn_iskarta_adet.png"),
};

const px = (v: number, s: number) => Math.round(v * s);

function formatDate(date: Date) {
  const day = String(date.getDate()).padStart(2, "0");
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const year = date.getFullYear();
  return `${day}.${month}.${year}`;
}

function addDays(date: Date, amount: number) {
  const nextDate = new Date(date);
  nextDate.setDate(nextDate.getDate() + amount);
  return nextDate;
}

const MACHINE_NAMES = ["MP550-001", "MP550-002", "MP550-003", "MP550-004", "MP550-005", "MP550-006"];

// ============================================================
// ÜRETİM ADET EKRANI - VERİLEN KOORDİNATLARA GÖRE
// ============================================================
function PatronDashboardScreen({ machineIndex, onBack }: { machineIndex: number; onBack: () => void }) {
  const { width, height } = useWindowDimensions();
  const scaleX = width / 420;
  const scaleY = height / 840;
  const scale = Math.min(scaleX, scaleY);
  const pxFunc = (v: number) => Math.round(v * scale);

  const machineName = MACHINE_NAMES[machineIndex];
  const isActive = machineIndex < 2;

  // Grafik için saatlik veri
  const saatlikVeri = [
    { saat: "12:00", uretim: 95, iskarta: 1 },
    { saat: "13:00", uretim: 98, iskarta: 0 },
    { saat: "14:00", uretim: 102, iskarta: 1 },
    { saat: "15:00", uretim: 89, iskarta: 2 },
    { saat: "16:00", uretim: 110, iskarta: 0 },
    { saat: "17:00", uretim: 105, iskarta: 1 },
    { saat: "18:00", uretim: 78, iskarta: 0 },
    { saat: "19:00", uretim: 73, iskarta: 0 },
  ];

  const maxUretim = Math.max(...saatlikVeri.map(v => v.uretim)) * 1.15;

  // Düzen sabitleri
  const grafikLeft = pxFunc(15);
  const kutuTop = pxFunc(165);
  const grafikTop = pxFunc(430);
  const grafikWidth = pxFunc(390);
  const grafikHeight = pxFunc(280);
  const grafikPaddingLeft = pxFunc(35);
  const grafikPaddingBottom = pxFunc(25);
  const grafikInnerWidth = grafikWidth - grafikPaddingLeft - pxFunc(10);
  const grafikInnerHeight = grafikHeight - grafikPaddingBottom - pxFunc(25);

  const getX = (index: number) => grafikPaddingLeft + (index / (saatlikVeri.length - 1)) * grafikInnerWidth;
  const getY = (value: number) => grafikPaddingBottom + grafikInnerHeight - (value / maxUretim) * grafikInnerHeight;

  return (
    <View style={{ flex: 1, backgroundColor: "#0B1E36" }}>
      <StatusBar style="light" />
      <Svg width={width} height={height} style={{ position: "absolute", left: 0, top: 0 }}>
        <Defs>
          <LinearGradient id="patronBg" x1="0" y1="0" x2="1" y2="1">
            <Stop offset="0" stopColor="#102B4B" />
            <Stop offset="0.5" stopColor="#0B1E36" />
            <Stop offset="1" stopColor="#08182C" />
          </LinearGradient>
        </Defs>
        <Rect x="0" y="0" width={width} height={height} fill="url(#patronBg)" />
      </Svg>

      {/* Üst Bar: Geri + Makine Adı + Fiş İkonu + Durum */}
      <View style={{ position: "absolute", left: pxFunc(15), top: pxFunc(35), right: pxFunc(15), flexDirection: "row", alignItems: "center", justifyContent: "space-between" }}>
        <Pressable onPress={onBack} style={{ width: pxFunc(45), height: pxFunc(45), justifyContent: "center" }}>
          <Image source={require("./üretim_adet/geri_oku.png")} resizeMode="contain" style={{ width: "100%", height: "100%" }} />
        </Pressable>
        <Text style={{ color: "#FFFFFF", fontSize: pxFunc(32), fontWeight: "700", textAlign: "center" }}>{machineName}</Text>
        <View style={{ alignItems: "center" }}>
          <Image source={require("./4. ekran/status_active.png")} resizeMode="contain" style={{ width: pxFunc(50), height: pxFunc(20) }} />
          <Text style={{ color: isActive ? "#95FF94" : "#FF7A7A", fontSize: pxFunc(11), fontWeight: "600", textShadowColor: isActive ? "#95FF94" : "#FF7A7A", textShadowRadius: 6, marginTop: pxFunc(4) }}>
            {isActive ? "Cihaz Aktif" : "Cihaz Pasif"}
          </Text>
        </View>
      </View>

      {/* İki Kutu Yan Yana - Sayılar büyük */}
      <View style={{ position: "absolute", left: pxFunc(20), right: pxFunc(20), top: kutuTop, flexDirection: "row", justifyContent: "space-between" }}>
        {/* Sol Yeşil Kutu - Üretim */}
        <View style={{ width: pxFunc(165), height: pxFunc(60) }}>
          <Image source={require("./üretim_adet/yeşil_kutu.png")} resizeMode="stretch" style={{ width: "100%", height: "100%" }} />
          <Text style={{ position: "absolute", top: 0, left: 0, right: 0, bottom: 0, color: "#FFFFFF", fontSize: pxFunc(36), fontWeight: "700", textAlign: "center", textAlignVertical: "center" }}>52</Text>
        </View>
        {/* Sağ Kırmızı Kutu - Iskarta */}
        <View style={{ width: pxFunc(165), height: pxFunc(60) }}>
          <Image source={require("./üretim_adet/kırmızı_kutu.png")} resizeMode="stretch" style={{ width: "100%", height: "100%" }} />
          <Text style={{ position: "absolute", top: 0, left: 0, right: 0, bottom: 0, color: "#FFFFFF", fontSize: pxFunc(36), fontWeight: "700", textAlign: "center", textAlignVertical: "center" }}>5</Text>
        </View>
      </View>

      {/* Grafik Başlığı */}
      <Text style={{ position: "absolute", left: pxFunc(20), top: pxFunc(405), color: "#FFFFFF", fontSize: pxFunc(14), fontWeight: "700" }}>Saatlik Üretim</Text>

      {/* Grafik container */}
      <View style={{ position: "absolute", left: grafikLeft, top: grafikTop, width: grafikWidth, height: grafikHeight, backgroundColor: "rgba(15, 35, 65, 0.5)", borderRadius: pxFunc(12), borderWidth: 1, borderColor: "rgba(60, 120, 200, 0.2)" }}>
        {/* Y ekseni etiketleri */}
        {[0, 25, 50, 75, 100].map((pct) => {
          const val = Math.round((pct / 100) * maxUretim);
          const yPos = grafikPaddingBottom + grafikInnerHeight - (pct / 100) * grafikInnerHeight;
          return (
            <Text key={pct} style={{ position: "absolute", left: pxFunc(2), top: yPos - pxFunc(6), color: "rgba(150, 180, 220, 0.6)", fontSize: pxFunc(8) }}>
              {val}
            </Text>
          );
        })}

        {/* Yatay grid çizgileri */}
        {[0, 25, 50, 75, 100].map((pct) => {
          const yPos = grafikPaddingBottom + (pct / 100) * grafikInnerHeight;
          return (
            <View key={pct} style={{ position: "absolute", left: grafikPaddingLeft, right: pxFunc(10), top: yPos, height: 1, backgroundColor: "rgba(80, 130, 200, 0.12)" }} />
          );
        })}

        {/* ÇİZGİ */}
        <Svg width={grafikWidth} height={grafikHeight} style={{ position: "absolute", left: 0, top: 0 }}>
          <Path d={`M ${saatlikVeri.map((v, i) => `${getX(i)},${getY(v.uretim)}`).join(" L ")}`} stroke="rgba(80, 200, 255, 0.3)" strokeWidth={pxFunc(8)} strokeLinecap="round" strokeLinejoin="round" fill="none" />
          <Path d={`M ${saatlikVeri.map((v, i) => `${getX(i)},${getY(v.uretim)}`).join(" L ")}`} stroke="#50C8FF" strokeWidth={pxFunc(3)} strokeLinecap="round" strokeLinejoin="round" fill="none" />
        </Svg>

        {/* NOKTALAR */}
        {saatlikVeri.map((v, i) => (
          <View key={i} style={{ position: "absolute", left: getX(i) - pxFunc(5), top: getY(v.uretim) - pxFunc(5) }}>
            <View style={{ width: pxFunc(10), height: pxFunc(10), borderRadius: pxFunc(5), backgroundColor: "rgba(80, 200, 255, 0.3)" }} />
            <View style={{ position: "absolute", left: pxFunc(1.5), top: pxFunc(1.5), width: pxFunc(7), height: pxFunc(7), borderRadius: pxFunc(3.5), backgroundColor: v.uretim < 85 ? "#FF6464" : v.uretim < 95 ? "#FFC850" : "#50C8FF", borderWidth: 2, borderColor: "#0B1E36" }} />
          </View>
        ))}

        {/* X ekseni etiketleri */}
        {saatlikVeri.map((v, i) => (
          <Text key={i} style={{ position: "absolute", left: getX(i) - pxFunc(18), top: grafikHeight - pxFunc(18), width: pxFunc(36), color: "rgba(150, 180, 220, 0.7)", fontSize: pxFunc(8), textAlign: "center" }}>
            {v.saat}
          </Text>
        ))}

        {/* Legend */}
        <View style={{ position: "absolute", right: pxFunc(12), top: pxFunc(8), flexDirection: "row", alignItems: "center" }}>
          <View style={{ width: pxFunc(12), height: pxFunc(3), backgroundColor: "#50C8FF", borderRadius: pxFunc(1.5), marginRight: pxFunc(4) }} />
          <Text style={{ color: "rgba(180, 220, 255, 0.8)", fontSize: pxFunc(9) }}>Üretim</Text>
        </View>
      </View>

      {/* MOSTRAVI LOGO */}
      <Image source={ASSETS.logo} resizeMode="contain" style={{ position: "absolute", left: pxFunc(155), bottom: pxFunc(15), width: pxFunc(110), height: pxFunc(28), opacity: 0.5 }} />
    </View>
  );
}

function MachineDetailScreen({ machineIndex, onBack, onUretimAdet }: { machineIndex: number; onBack: () => void; onUretimAdet: () => void }) {
  const { width, height } = useWindowDimensions();
  const detailScale = Math.min(width / DETAIL_SCREEN_WIDTH, height / DETAIL_SCREEN_HEIGHT);
  const detailRenderedWidth = px(DETAIL_SCREEN_WIDTH, detailScale);
  const detailRenderedHeight = px(DETAIL_SCREEN_HEIGHT, detailScale);
  const detailLeft = Math.round((width - detailRenderedWidth) / 2);
  const detailTop = Math.round((height - detailRenderedHeight) / 2);
  const detailPx = (value: number) => px(value, detailScale);
  const [currentDate, setCurrentDate] = useState(new Date(2026, 3, 14));
  const machineName = MACHINE_NAMES[machineIndex];
  const isActive = machineIndex < 2;

  return (
    <View style={{ flex: 1, backgroundColor: DETAIL_BACKGROUND }}>
      <StatusBar style="light" />
      <Svg width={width} height={height} style={{ position: "absolute", left: 0, top: 0 }}>
        <Defs>
          <LinearGradient id="detailBackgroundGradient" x1="0" y1="0" x2="1" y2="1">
            <Stop offset="0" stopColor="#102B4B" />
            <Stop offset="0.5" stopColor="#0B1E36" />
            <Stop offset="1" stopColor="#08182C" />
          </LinearGradient>
        </Defs>
        <Rect x="0" y="0" width={width} height={height} fill="url(#detailBackgroundGradient)" />
      </Svg>

      <Pressable onPress={onBack} style={{ position: "absolute", left: detailPx(22.7), top: detailPx(50), width: detailPx(32), height: detailPx(32) }}>
        <Image source={ASSETS.detailBackArrow} resizeMode="contain" style={{ width: "100%", height: "100%" }} />
      </Pressable>

      <View style={{ position: "absolute", left: detailLeft, top: detailTop, width: detailRenderedWidth, height: detailRenderedHeight }}>
        <Text style={{ position: "absolute", left: detailPx(70), top: detailPx(5), width: detailPx(280), height: detailPx(60), color: "#FFFFFF", fontSize: detailPx(34), fontWeight: "700", textAlign: "center", textAlignVertical: "center", includeFontPadding: false }}>
          {machineName}
        </Text>

        <Pressable onPress={() => setCurrentDate((prevDate) => addDays(prevDate, -1))} style={{ position: "absolute", left: detailPx(55), top: detailPx(132.9), width: detailPx(40), height: detailPx(35) }}>
          <Image source={ASSETS.detailArrowLeft} resizeMode="contain" style={{ width: "100%", height: "100%" }} />
        </Pressable>

        <View style={{ position: "absolute", left: detailPx(105), top: detailPx(124), width: detailPx(210), height: detailPx(45), borderRadius: detailPx(12), backgroundColor: "rgba(150, 198, 236, 0.14)", borderWidth: 1, borderColor: "rgba(188, 229, 255, 0.25)", alignItems: "center", justifyContent: "center" }}>
          <Text style={{ color: "#FFFFFF", fontSize: detailPx(22), fontWeight: "600", letterSpacing: 0.3 }}>
            {formatDate(currentDate)}
          </Text>
        </View>

        <Pressable onPress={() => setCurrentDate((prevDate) => addDays(prevDate, 1))} style={{ position: "absolute", left: detailPx(325), top: detailPx(132.9), width: detailPx(40), height: detailPx(35) }}>
          <Image source={ASSETS.detailArrowRight} resizeMode="contain" style={{ width: "100%", height: "100%" }} />
        </Pressable>

        <Image source={ASSETS.detailStatusActive} resizeMode="contain" style={{ position: "absolute", left: detailPx(330.4), top: detailPx(56.1), width: detailPx(50), height: detailPx(19.3) }} />

        <Text style={{ position: "absolute", left: detailPx(322.2), top: detailPx(79.9), width: detailPx(80.4), height: detailPx(14.3), color: "#95FF94", fontSize: detailPx(9.5), textAlign: "center", textAlignVertical: "center", includeFontPadding: false, textShadowColor: "#95FF94", textShadowRadius: 6, textShadowOffset: { width: 0, height: 0 } }}>
          {isActive ? "Cihaz Aktif" : "Cihaz Pasif"}
        </Text>

        <Text style={{ position: "absolute", left: detailPx(310), top: detailPx(96), width: detailPx(90), height: detailPx(7.4), color: "rgba(200, 220, 255, 0.7)", fontSize: detailPx(7), textAlign: "right", textAlignVertical: "center", includeFontPadding: false }}>
          Son Güncelleme
        </Text>

        <Text style={{ position: "absolute", left: detailPx(310), top: detailPx(107), width: detailPx(90), height: detailPx(9), color: "#FFFFFF", fontSize: detailPx(9), textAlign: "right", textAlignVertical: "center", includeFontPadding: false }}>
          21.04.2026 : 19.25
        </Text>

        <Pressable onPress={onUretimAdet} style={{ position: "absolute", left: detailPx(80), top: detailPx(265), width: detailPx(260), height: detailPx(80) }}>
          <Image source={ASSETS.detailProductionQty} resizeMode="stretch" style={{ width: "100%", height: "100%" }} />
        </Pressable>

        <Image source={ASSETS.detailProductionTimes} resizeMode="stretch" style={{ position: "absolute", left: detailPx(80), top: detailPx(400), width: detailPx(260), height: detailPx(80) }} />

        <Image source={ASSETS.detailEfficiency} resizeMode="stretch" style={{ position: "absolute", left: detailPx(80), top: detailPx(535), width: detailPx(260), height: detailPx(80) }} />

        <Image source={ASSETS.detailScrapQty} resizeMode="stretch" style={{ position: "absolute", left: detailPx(80), top: detailPx(680), width: detailPx(260), height: detailPx(80) }} />
      </View>
    </View>
  );
}

function NeonPlug({ active }: { active: boolean }) {
  const glowColor = active ? "#30FF75" : "#FF5A5A";
  const coreColor = active ? "#F8FFF8" : "#FFF6F6";
  const borderColor = active ? "rgba(92,255,152,0.42)" : "rgba(255,118,118,0.34)";
  const plugPaths = [
    "M12 22v-5",
    "M9 8V2",
    "M15 8V2",
    "M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8Z",
  ];

  return (
    <View pointerEvents="none" style={styles.plugBox}>
      <Image source={active ? require("./assets/images/plug-active.png") : require("./assets/images/plug-passive.png")} width={PLUG_IMG_WIDTH} height={PLUG_IMG_HEIGHT} style={{ position: "absolute", left: 0, top: 0 }} resizeMode="contain" />
      <Svg width={PLUG_PANEL_WIDTH} height={PLUG_PANEL_HEIGHT} style={{ position: "absolute", left: 0, top: 0 }} viewBox="0 0 54 34">
        <Defs>
          <LinearGradient id="panelOuter" x1="0" y1="0" x2="1" y2="1">
            <Stop offset="0" stopColor="#7E8792" stopOpacity="0.9" />
            <Stop offset="0.45" stopColor="#4B5562" stopOpacity="0.98" />
            <Stop offset="1" stopColor="#8A94A1" stopOpacity="0.95" />
          </LinearGradient>
          <LinearGradient id="panelInner" x1="0" y1="0" x2="1" y2="1">
            <Stop offset="0" stopColor="#2A3544" />
            <Stop offset="1" stopColor="#1A2432" />
          </LinearGradient>
        </Defs>
        <Rect x="0.6" y="0.6" width="52.8" height="32.8" rx="11" fill="url(#panelOuter)" />
        <Rect x="3.4" y="3.4" width="47.2" height="27.2" rx="9.2" fill="url(#panelInner)" />
        <Rect x="3.4" y="3.4" width="47.2" height="27.2" rx="9.2" stroke={borderColor} strokeWidth="0.7" />
        <G transform="translate(16 4) rotate(-28 12 12) scale(0.95)">
          {plugPaths.map((d) => (
            <Path key={`${d}-g1`} d={d} stroke={glowColor} strokeWidth="10" strokeLinecap="round" strokeLinejoin="round" opacity="0.14" />
          ))}
          {plugPaths.map((d) => (
            <Path key={`${d}-g2`} d={d} stroke={glowColor} strokeWidth="6.5" strokeLinecap="round" strokeLinejoin="round" opacity="0.35" />
          ))}
          {plugPaths.map((d) => (
            <Path key={`${d}-c`} d={d} stroke={coreColor} strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
          ))}
        </G>
      </Svg>
    </View>
  );
}

function StatusBadge({ active, label, fontSize }: { active: boolean; label: string; fontSize: number }) {
  const glowColor = active ? "#95FF94" : "#FF7A7A";
  const softColor = active ? "rgba(149,255,148,0.4)" : "rgba(255,122,122,0.35)";
  const textColor = active ? "#C7FFB6" : "#FFADAD";
  const coreColor = active ? "#EDFFE5" : "#FFF1F1";

  return (
    <View pointerEvents="none" style={styles.statusBadge}>
      <Image source={active ? require("./assets/images/badge-active.png") : require("./assets/images/badge-passive.png")} width={BADGE_IMG_WIDTH} height={BADGE_IMG_HEIGHT} style={{ position: "absolute", left: 0, top: 0 }} resizeMode="contain" />
      <Text style={{ position: "absolute", color: softColor, fontSize, fontWeight: "400", textAlign: "center", textShadowColor: glowColor, textShadowRadius: 18, textShadowOffset: { width: 0, height: 0 }, opacity: 0.95 }}>
        {label}
      </Text>
      <Text style={{ position: "absolute", color: textColor, fontSize, fontWeight: "400", textAlign: "center", textShadowColor: glowColor, textShadowRadius: 9, textShadowOffset: { width: 0, height: 0 } }}>
        {label}
      </Text>
      <Text style={{ color: coreColor, fontSize, fontWeight: "400", textAlign: "center" }}>
        {label}
      </Text>
    </View>
  );
}

const SUPABASE_URL = "https://fnzfzlmcyfulggtthhgh.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZuemZ6bG1jeWZ1bGdndHRoaGdoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzk4MjIzOTcsImV4cCI6MjA5NTM5ODM5N30.wYS5-HWGiqTizyiwawkY15xDCVYhROhuVZ1u_kdlt00";

async function supabaseLogin(email: string, password: string): Promise<{ user: unknown; error: string | null }> {
  try {
    const res = await fetch(`${SUPABASE_URL}/auth/v1/token?grant_type=password`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        apikey: SUPABASE_ANON_KEY,
        Authorization: `Bearer ${SUPABASE_ANON_KEY}`,
      },
      body: JSON.stringify({ email, password }),
    });

    let data: unknown;
    try {
      data = await res.json();
    } catch {
      data = null;
    }

    if (!res.ok || (data && typeof data === "object" && "error" in data)) {
      const errObj = data && typeof data === "object" ? (data as Record<string, unknown>) : {};
      const msg = String(errObj.error_description || errObj.error || "Giris basarisiz.");
      const turkishMsg = msg === "Invalid login credentials" ? "E-posta veya sifre hatali."
        : msg === "Email not confirmed" ? "E-posta dogrulanmamis."
        : msg === "User already registered" ? "Bu e-posta zaten kayitli."
        : msg === "Signup requires a valid password" ? "Gecerli bir sifre girin."
        : msg === "Signup requires a valid email" ? "Gecerli bir e-posta girin."
        : msg === "Failed to fetch" ? "Sunucuya baglanilamadi. Internet baglantinizi kontrol edin."
        : msg;
      return { user: null, error: turkishMsg };
    }

    if (data && typeof data === "object" && "user" in data) {
      return { user: (data as { user: unknown }).user, error: null };
    }

    return { user: null, error: "Beklenmeyen cevap." };
  } catch (e: unknown) {
    const msg = e instanceof Error ? e.message : "Bilinmeyen hata olustu.";
    return { user: null, error: msg === "Failed to fetch" ? "Sunucuya baglanilamadi. Internet baglantinizi kontrol edin." : msg };
  }
}

export default function App() {
  const { width, height } = useWindowDimensions();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [remember, setRemember] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");
  const [currentScreen, setCurrentScreen] = useState<"login" | "home" | "machines" | "machineDetail" | "patronDashboard">("login");
  const [currentMachine, setCurrentMachine] = useState(0);

  const scale = Math.min(width / BASE_WIDTH, 1);
  const shiftDown = Math.round(-30 * scale);
  const homeImageScale = Math.min(width / HOME_IMAGE_WIDTH, height / HOME_IMAGE_HEIGHT);
  const homeRenderedWidth = Math.round(HOME_IMAGE_WIDTH * homeImageScale);
  const homeRenderedHeight = Math.round(HOME_IMAGE_HEIGHT * homeImageScale);
  const homeImageLeft = Math.round((width - homeRenderedWidth) / 2);
  const homeImageTop = Math.round((height - homeRenderedHeight) / 2);

  async function handleLogin() {
    if (!email || !password) {
      setErrorMsg("Lutfen e-posta ve sifre girin.");
      return;
    }
    setIsLoading(true);
    setErrorMsg("");

    const { error } = await supabaseLogin(email, password);

    setIsLoading(false);

    if (error) {
      setErrorMsg(error);
      return;
    }

    setCurrentScreen("home");
  }

  if (currentScreen === "home") {
    return (
      <SafeAreaView style={styles.safe}>
        <StatusBar style="light" />
        <View style={{ flex: 1, width: "100%", height: "100%" }}>
          <View style={{ position: "absolute", left: homeImageLeft, top: homeImageTop, width: homeRenderedWidth, height: homeRenderedHeight }}>
            <Image source={require("./2. sayfa/png/mostravi yapay zeka (orjinal) (1).png")} resizeMode="contain" style={{ width: "100%", height: "100%" }} />
            <Pressable onPress={() => setCurrentScreen("machines")} style={{ position: "absolute", left: `${HOME_BUTTON_AREAS[0].left}%`, top: `${HOME_BUTTON_AREAS[0].top}%`, width: `${HOME_BUTTON_AREAS[0].width}%`, height: `${HOME_BUTTON_AREAS[0].height}%`, backgroundColor: HOME_DEBUG_HITBOX_COLOR }} />
            <Pressable onPress={() => {}} style={{ position: "absolute", left: `${HOME_BUTTON_AREAS[1].left}%`, top: `${HOME_BUTTON_AREAS[1].top}%`, width: `${HOME_BUTTON_AREAS[1].width}%`, height: `${HOME_BUTTON_AREAS[1].height}%`, backgroundColor: HOME_DEBUG_HITBOX_COLOR }} />
            <Pressable onPress={() => {}} style={{ position: "absolute", left: `${HOME_BUTTON_AREAS[2].left}%`, top: `${HOME_BUTTON_AREAS[2].top}%`, width: `${HOME_BUTTON_AREAS[2].width}%`, height: `${HOME_BUTTON_AREAS[2].height}%`, backgroundColor: HOME_DEBUG_HITBOX_COLOR }} />
            <Pressable onPress={() => {}} style={{ position: "absolute", left: `${HOME_BUTTON_AREAS[3].left}%`, top: `${HOME_BUTTON_AREAS[3].top}%`, width: `${HOME_BUTTON_AREAS[3].width}%`, height: `${HOME_BUTTON_AREAS[3].height}%`, backgroundColor: HOME_DEBUG_HITBOX_COLOR }} />
          </View>
        </View>
      </SafeAreaView>
    );
  }
  if (currentScreen === "machines") {
    const labelFontSize = Math.round(14 * scale);

    return (
      <View style={{ flex: 1, backgroundColor: BACKGROUND }}>
        <View style={{ flex: 1 }}>
          <Image source={require("./makineler ekranı(3. ekran)/png/mostravi yapay zeka (orjinal) Kopyası (2).png")} resizeMode="cover" style={{ position: "absolute", left: 0, top: 0, width: "100%", height: "100%" }} />
          <View style={{ position: "absolute", left: "3.5%", top: "1.5%", width: "25%", height: "3%", backgroundColor: BACKGROUND }} />
          <View style={{ position: "absolute", left: "15%", top: "5.2%", backgroundColor: BACKGROUND, paddingHorizontal: 8, paddingVertical: 2 }}>
            <Text style={{ color: "#FFFFFF", fontSize: labelFontSize * 2.4, fontWeight: "700", letterSpacing: 1 }}>
              MAKİNELERİM
            </Text>
          </View>
          {MACHINE_HITBOXES.map((hitbox, index) => (
            <Pressable key={MACHINE_NAMES[index]} onPress={() => { setCurrentMachine(index); setCurrentScreen("machineDetail"); }} style={{ position: "absolute", left: `${(hitbox.left / MACHINES_IMAGE_WIDTH) * 100}%`, top: `${(hitbox.top / MACHINES_IMAGE_HEIGHT) * 100}%`, width: `${(hitbox.width / MACHINES_IMAGE_WIDTH) * 100}%`, height: `${(hitbox.height / MACHINES_IMAGE_HEIGHT) * 100}%`, backgroundColor: "transparent" }} />
          ))}
          {MACHINE_LABELS.map((machine) => (
            <Text key={machine.name} style={{ position: "absolute", left: `${(machine.left / MACHINES_IMAGE_WIDTH) * 100}%`, top: `${(machine.top / MACHINES_IMAGE_HEIGHT) * 100}%`, color: "#FFFFFF", fontSize: labelFontSize, fontWeight: "700" }}>
              {machine.name}
            </Text>
          ))}
          {STATUS_LABELS.map((status) => (
            <View key={status.name} style={{ position: "absolute", left: `${(status.left / MACHINES_IMAGE_WIDTH) * 100}%`, top: `${(status.top / MACHINES_IMAGE_HEIGHT) * 100}%` }}>
              <StatusBadge active={status.active} label={status.label} fontSize={labelFontSize * 0.85} />
            </View>
          ))}
        </View>
      </View>
    );
  }
  if (currentScreen === "machineDetail") {
    return (
      <MachineDetailScreen machineIndex={currentMachine} onBack={() => setCurrentScreen("machines")} onUretimAdet={() => setCurrentScreen("patronDashboard")} />
    );
  }
  if (currentScreen === "patronDashboard") {
    return (
      <PatronDashboardScreen machineIndex={currentMachine} onBack={() => setCurrentScreen("machineDetail")} />
    );
  }

  return (
    <SafeAreaView style={styles.safe}>
      <StatusBar style="light" />
      <View style={[styles.root, { backgroundColor: BACKGROUND }]}>

        {isLoading && (
          <View style={styles.loadingOverlay}>
            <ActivityIndicator size="large" color="#E8FFF2" />
          </View>
        )}

        <View style={{ position: "absolute", left: 0, right: 0, top: 0, bottom: 0, transform: [{ translateY: shiftDown }] }}>
          <Image source={ASSETS.logo} resizeMode="contain" style={{ position: "absolute", left: px(51.4, scale), top: px(158.3, scale), width: px(290, scale), height: px(63, scale) }} />

          <Text style={{ position: "absolute", left: px(51.4 + 290 - 85 + 5, scale), top: px(227.7, scale), width: px(85, scale), height: px(13, scale), color: "#FFF", fontSize: px(8.2, scale), textAlign: "right" }}>yapay zeka dunyasi</Text>

          <Text style={{ position: "absolute", left: px(116.7, scale), top: px(316.5, scale), width: px(215.5, scale), height: px(27.3, scale), color: "#FFF", fontSize: px(17.4, scale), fontWeight: "700", textAlign: "center" }}>E-Posta Adresi</Text>

          <View style={{ position: "absolute", left: px(57.9, scale), top: px(368.8, scale), width: px(316.5, scale), height: px(54.2, scale) }}>
            <Image source={ASSETS.emailInput} resizeMode="stretch" style={{ width: "100%", height: "100%" }} />
            <TextInput value={email} onChangeText={(t) => { setEmail(t); setErrorMsg(""); }} placeholder="........" placeholderTextColor={PLACEHOLDER} keyboardType="email-address" autoCapitalize="none" autoCorrect={false} selectionColor="#D7FFF0" style={{ position: "absolute", left: px(20, scale), right: px(58, scale), top: 0, bottom: 0, color: INPUT_TEXT, fontSize: px(15, scale), fontWeight: "600" }} />
          </View>

          <Text style={{ position: "absolute", left: px(191.9, scale), top: px(448, scale), width: px(50.5, scale), height: px(20.4, scale), color: "#FFF", fontSize: px(13, scale), fontWeight: "700", textAlign: "center" }}>Sifre</Text>

          <View style={{ position: "absolute", left: px(59, scale), top: px(487.7, scale), width: px(316.5, scale), height: px(54.2, scale) }}>
            <Image source={ASSETS.passwordInput} resizeMode="stretch" style={{ width: "100%", height: "100%" }} />
            <TextInput value={password} onChangeText={(t) => { setPassword(t); setErrorMsg(""); }} placeholder="........" placeholderTextColor={PLACEHOLDER} autoCapitalize="none" autoCorrect={false} secureTextEntry selectionColor="#D7FFF0" style={{ position: "absolute", left: px(20, scale), right: px(58, scale), top: 0, bottom: 0, color: INPUT_TEXT, fontSize: px(15, scale), fontWeight: "600" }} />
          </View>

          {errorMsg ? (
            <Text style={{ position: "absolute", left: px(57.9, scale), top: px(547, scale), width: px(316.5, scale), color: ERROR_COLOR, fontSize: px(12, scale), textAlign: "center" }}>{errorMsg}</Text>
          ) : null}

          <Pressable onPress={handleLogin} style={{ position: "absolute", left: px(110.3, scale), top: px(573.9, scale), width: px(193.4, scale), height: px(83, scale), alignItems: "center", justifyContent: "center" }}>
            <Image source={ASSETS.button} resizeMode="stretch" style={{ width: "100%", height: "100%" }} />
            <Text style={{ position: "absolute", color: BUTTON_TEXT, fontSize: px(18.3, scale), fontWeight: "700", letterSpacing: px(0.25, scale) }}>GIRIS YAP</Text>
          </Pressable>

          <Pressable onPress={() => setRemember(r => !r)} style={{ position: "absolute", left: px(332.2, scale), top: px(677.9, scale), width: px(20.5, scale), height: px(20.5, scale), alignItems: "center", justifyContent: "center" }}>
            <Image source={ASSETS.checkbox} resizeMode="stretch" style={{ width: "100%", height: "100%" }} />
            {remember ? <View style={{ position: "absolute", width: px(11, scale), height: px(11, scale), backgroundColor: "#FFF" }} /> : null}
          </Pressable>

          <Text style={{ position: "absolute", left: px(310.6, scale), top: px(717.6, scale), width: px(63.8, scale), height: px(40.4, scale), color: "#FFF", fontSize: px(13, scale), fontWeight: "700", lineHeight: px(15, scale), textAlign: "center" }}>Sifre{"\n"}Kaydet</Text>
        </View>

        <Image source={ASSETS.banner} resizeMode="stretch" style={{ position: "absolute", left: 0, bottom: 0, width, height: px(47, scale) }} />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: BACKGROUND },
  root: { flex: 1 },
  plugBox: {
    width: PLUG_PANEL_WIDTH,
    height: PLUG_PANEL_HEIGHT,
  },
  statusBadge: {
    minWidth: 108,
    paddingHorizontal: 2,
    paddingVertical: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  loadingOverlay: {
    position: "absolute",
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: "rgba(3, 28, 58, 0.7)",
    justifyContent: "center",
    alignItems: "center",
    zIndex: 999,
  },
});

