import IconPencilFill from "~icons/mingcute/pencil-fill";
import IconInformationFill from "~icons/mingcute/information-fill";
import IconBulbFill from "~icons/mingcute/bulb-fill";
import IconAlertFill from "~icons/mingcute/alert-fill";
import IconFireFill from "~icons/mingcute/fire-fill";
import styles from "./Admonition.module.css";
import { twMerge } from "tailwind-merge";

export interface AdmonitionProps
  extends Omit<
    React.PropsWithChildren<React.ComponentPropsWithoutRef<"div">>,
    "title"
  > {
  type: "note" | "info" | "tip" | "caution" | "danger";
  title?: string;
  icon?: React.ReactNode;
}

function getDefaultInfo(type: AdmonitionProps["type"]) {
  switch (type) {
    case "note":
      return {
        title: "Note",
        icon: <IconPencilFill className="mr-2" />,
        className: styles.note,
      };
    case "info":
      return {
        title: "Info",
        icon: <IconInformationFill className="mr-2" />,
        className: styles.info,
      };
    case "tip":
      return {
        title: "Tips",
        icon: <IconBulbFill className="mr-2" />,
        className: styles.tip,
      };
    case "caution":
      return {
        title: "Caution",
        icon: <IconAlertFill className="mr-2" />,
        className: styles.caution,
      };
    case "danger":
      return {
        title: "Danger",
        icon: <IconFireFill className="mr-2" />,
        className: styles.danger,
      };
    default:
      return null;
  }
}

export default function Admonition({
  type,
  title,
  icon,
  className,
  children,
  ...rest
}: AdmonitionProps) {
  const defaultInfo = getDefaultInfo(type);
  if (defaultInfo === null) {
    return <>{children}</>;
  }
  const displayTitle = title ?? defaultInfo.title;
  const displayIcon = icon ?? defaultInfo.icon;

  return (
    <div
      className={twMerge(
        "my-4 rounded-lg px-4 py-2",
        defaultInfo.className,
        className,
      )}
      {...rest}
    >
      <div className="flex items-center text-base font-bold">
        {displayIcon}
        {displayTitle}
      </div>
      <div className="mt-2 prose-compact text-sm">{children}</div>
    </div>
  );
}
