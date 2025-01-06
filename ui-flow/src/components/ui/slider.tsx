import * as React from "react";
import * as SliderPrimitive from "@radix-ui/react-slider";

import { cn } from "@/lib/utils";

const Slider = React.forwardRef<
    React.ElementRef<typeof SliderPrimitive.Root>,
    React.ComponentPropsWithoutRef<typeof SliderPrimitive.Root>
>(({ className, ...props }, ref) => (
    <SliderPrimitive.Root
        ref={ref}
        className={cn(
            "relative flex w-full touch-none select-none items-center",
            className
        )}
        {...props}
    >
        <SliderPrimitive.Track className="relative h-1.5 w-full grow overflow-hidden rounded-full bg-primary/20">
            <SliderPrimitive.Range className="absolute h-full bg-primary" />
        </SliderPrimitive.Track>
        <SliderPrimitive.Thumb className="block h-4 w-4 rounded-full border border-primary/50 bg-background shadow transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50" />
    </SliderPrimitive.Root>
));
Slider.displayName = SliderPrimitive.Root.displayName;

type FlowSliderProps = React.ComponentPropsWithoutRef<
    typeof SliderPrimitive.Root
> & {
    label: string;
};

const FlowSlider = React.forwardRef<
    React.ElementRef<typeof SliderPrimitive.Root>,
    FlowSliderProps
>(({ className, label, ...props }, ref) => (
    <div className="relative">
        <SliderPrimitive.Root
            ref={ref}
            className={cn(
                "relative flex w-full touch-none select-none items-center z-10",
                className
            )}
            {...props}
        >
            <SliderPrimitive.Track className="relative h-6 w-full grow overflow-hidden rounded bg-primary/30">
                <SliderPrimitive.Range className="absolute h-full bg-primary" />
            </SliderPrimitive.Track>
            <SliderPrimitive.Thumb className="block h-7 w-3 rounded border border-primary/50 bg-background shadow transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50" />
        </SliderPrimitive.Root>
        <div className="absolute top-1 left-2 text-[12px] text-background z-20">{label}</div>
    </div>
));
FlowSlider.displayName = "FlowSlider";

export { Slider, FlowSlider };
