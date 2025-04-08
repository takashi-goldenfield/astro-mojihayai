import {
  Icon as Iconify,
  type IconProps as IconifyProps,
} from "@iconify/react";

export interface IconProps extends Omit<IconifyProps, "icon"> {
  name: string;
}
export default function Icon({ name, ...rest }: IconProps) {
  return <Iconify {...rest} icon={name} />;
}
