import { useEffect, useState } from "react";

// Télécharge entièrement les vidéos puis renvoie des URLs locales (blob).
// blobs === null tant que tout n'est pas chargé ; progress va de 0 à 1.
export function useVideoPreload(urls) {
  const [blobs, setBlobs] = useState(null);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    let cancelled = false;
    const created = [];
    const loaded = urls.map(() => 0);
    const totals = urls.map(() => 0);

    const update = () => {
      const total = totals.reduce((a, b) => a + b, 0);
      if (total) setProgress(loaded.reduce((a, b) => a + b, 0) / total);
    };

    Promise.all(
      urls.map(async (url, i) => {
        const res = await fetch(url);
        totals[i] = Number(res.headers.get("content-length")) || 0;
        const reader = res.body.getReader();
        const chunks = [];
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          if (cancelled) {
            reader.cancel();
            return url;
          }
          chunks.push(value);
          loaded[i] += value.length;
          update();
        }
        const type = res.headers.get("content-type") || "video/mp4";
        const blobUrl = URL.createObjectURL(new Blob(chunks, { type }));
        created.push(blobUrl);
        return blobUrl;
      })
    )
      .then((result) => {
        if (cancelled) return;
        setProgress(1);
        setBlobs(result);
      })
      .catch(() => {
        // En cas d'erreur réseau, on retombe sur les URLs normales
        if (!cancelled) setBlobs(urls);
      });

    return () => {
      cancelled = true;
      created.forEach((u) => URL.revokeObjectURL(u));
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return { blobs, progress };
}
