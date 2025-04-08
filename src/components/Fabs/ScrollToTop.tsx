import IconChevronUp from "~icons/tabler/chevron-up";
import { useWindowScroll } from "react-use";
import useSSR from "@/hooks/useSSR";
import NoSSR from "../NoSSR";
type ScrollToTopProps = Record<string, never>;

export default function ScrollToTop({ ...rest }: ScrollToTopProps) {
  const { isBrowser } = useSSR();
  const { y: scrollY } = useWindowScroll();
  const getDasharray = () => {
    const r = 11;
    const perimeter = Math.PI * 2 * r;
    const pageLength = isBrowser
      ? document.documentElement.scrollHeight -
        document.documentElement.clientHeight +
        0.001
      : Number.POSITIVE_INFINITY;
    return `${(scrollY / pageLength) * perimeter} ${perimeter}`;
  };
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };
  return (
    <button
      type="button"
      className="relative w-11 h-11 bg-white dark:bg-gray-700 plate-shadow border-highlight rounded-full flex items-center justify-center"
      onClick={scrollToTop}
      aria-label="Scroll To Top"
    >
      <IconChevronUp className="w-6 h-6 z-10" />
      <NoSSR>
        <svg
          className="w-full h-full absolute"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <title>I'm title</title>
          <linearGradient id="Gradient" gradientTransform="rotate(90)">
            <stop
              offset="0"
              stopColor="currentColor"
              stopOpacity="1"
              className="text-primary-500"
            />
            <stop
              offset="1"
              stopColor="currentColor"
              stopOpacity="1"
              className="text-secondary-500"
            />
          </linearGradient>
          <circle
            stroke="url(#Gradient)"
            cx="12"
            cy="12"
            r="11"
            fill="none"
            strokeWidth={scrollY === 0 ? 0 : 2}
            strokeLinecap="round"
            strokeDasharray={getDasharray()}
            transform="rotate(-90, 12, 12)"
          />
        </svg>
      </NoSSR>
    </button>
  );
}
// No props are required for ScrollToTop component
