import { format } from "date-fns";
import { enUS } from "date-fns/locale";
export interface DateTimeProps {
  date: Date;
}

export default function DateTime({ date }: DateTimeProps) {
  const dateString = format(date, "PPP", {
    locale: enUS,
  });
  return <>{dateString}</>;
}
