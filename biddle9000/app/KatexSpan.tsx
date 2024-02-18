"use client";

import renderMathInElement from 'katex/dist/contrib/auto-render';

import 'katex/dist/katex.min.css';
import { useEffect, useRef } from 'react';

export default function KatexSpan({ text, ...delegated }: { text: string, [key: string]: any }) {
  const katexTextRef = useRef<HTMLDivElement | null>(null);

  // replace \n in text with newlines
  text = text.replace(/\\n/g, '\n');

  useEffect(() => {
    if (katexTextRef.current) {
      renderMathInElement(katexTextRef.current, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
        ],
      });
    }
  }, [text]);

  return (
    <div ref={katexTextRef} {...delegated} className="w-1/2">
      {text}
    </div>
  );
}