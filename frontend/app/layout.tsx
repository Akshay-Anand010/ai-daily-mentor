import "./globals.css";
import Link from "next/link";
export const metadata = { title: "AI Daily Mentor", description: "Your daily AI learning habit" };
export default function Layout({children}:{children:React.ReactNode}) { return <html lang="en"><body><header className="border-b border-slate-800"><nav className="mx-auto flex max-w-6xl items-center justify-between p-5"><Link href="/" className="font-bold tracking-tight">✦ AI Daily Mentor</Link><div className="flex gap-5 text-sm text-slate-300"><Link href="/archive">Archive</Link><Link href="/progress">Progress</Link><Link href="/settings">Settings</Link></div></nav></header><main className="mx-auto max-w-6xl p-5 md:p-10">{children}</main></body></html> }
