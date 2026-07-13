"use client";
import {useEffect,useState} from "react";
const api=process.env.NEXT_PUBLIC_API_URL||"";
type Lesson={id:number;title:string;topic:string;difficulty:string};
export default function Archive(){const [lessons,setLessons]=useState<Lesson[]>([]);useEffect(()=>{if(api)fetch(`${api}/api/lessons`).then(r=>r.json()).then(setLessons).catch(()=>{})},[]);return <><h1 className="text-3xl font-bold">Lesson archive</h1><p className="mt-2 text-slate-400">Searchable history of your AI learning journey.</p><div className="mt-7 grid gap-4">{lessons.map(l=><article key={l.id} className="rounded-xl border border-slate-800 p-5"><p className="text-sm text-cyan-300">{l.topic} · {l.difficulty}</p><h2 className="mt-1 text-xl font-semibold">{l.title}</h2><a className="mt-3 inline-block text-sm text-cyan-300" href={`${api}/api/lessons/${l.id}/pdf`}>Download PDF →</a></article>)}{!lessons.length&&<p className="mt-8 text-slate-400">Lessons will appear here when the API is configured.</p>}</div></>}
