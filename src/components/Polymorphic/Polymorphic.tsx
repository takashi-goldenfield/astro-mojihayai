import { forwardRef } from "react";
type ElementType = React.ElementType;
type Merge<A, B> = B & Omit<A, keyof B>;
export type PolymorphicProps<E extends ElementType, P> = Merge<
  React.ComponentPropsWithRef<E>,
  P & { as?: E }
>;
export type PolymorphicRef<E extends ElementType> =
  React.ComponentPropsWithRef<E>["ref"];

export function withPolymorphic<DefaultType extends ElementType, OwnProps = {}>(
  conponent: React.ComponentType<
    Merge<React.HTMLAttributes<HTMLElement>, OwnProps>
  >
) {
  type ComponentProps<E extends ElementType> = PolymorphicProps<E, OwnProps>;
  type PolymorphicComponent = <E extends ElementType = DefaultType>(
    props: ComponentProps<E>
  ) => React.ReactElement | null;

  return conponent as PolymorphicComponent;
}

const Polymorphic = forwardRef<
  HTMLDivElement,
  React.PropsWithChildren<{ as?: any }>
>(({ as, ...rest }, ref) => {
  const Element = as || "div";
  return <Element ref={ref} {...rest} />;
});

export default withPolymorphic<"div", React.PropsWithChildren<{}>>(Polymorphic);
