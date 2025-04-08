"use client";
import { getDefaultConfig } from "@rainbow-me/rainbowkit";
import {
  mainnet,
  sepolia,
  polygon,
  polygonMumbai,
  optimism,
  optimismGoerli,
  arbitrum,
  arbitrumGoerli,
  linea,
  lineaTestnet,
  base,
  baseGoerli,
  bsc,
  bscTestnet,
} from "wagmi/chains";

import linea_logo from "@/assets/linea.svg";
import lineaTesnet_logo from "@/assets/linea-seeklogo.png";
import zksync_logo from "@/assets/zkSync-logo.webp";

const walletConnectProjectId = "2d48cc7e378d709a2d971130a4de852d";

export const config = getDefaultConfig({
  appName: "RainbowKit demo",
  projectId: walletConnectProjectId,
  chains: [mainnet, polygon, optimism, arbitrum, base],
});
