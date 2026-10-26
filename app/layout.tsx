import Link from "next/link";
import "./globals.css";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="mx-auto max-w-5xl p-6">
        <nav className="mb-6 flex gap-2 border-b">
          <Link href="/" className="px-4 py-2">Price Tracker</Link>
          <Link href="/legacy" className="px-4 py-2">Legacy: 3DS EDA (2024)</Link>
        </nav>
        {children}
      </body>
    </html>
  );
}
