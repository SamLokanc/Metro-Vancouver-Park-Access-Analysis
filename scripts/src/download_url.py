import os
import requests

def download_url(url, filename, out_dir=os.path.join("data", "raw"), timeout=30) -> bool:
    """
    Downloads data from a URL with a specified filename.

    Parameters
    ----------
    url : str
        URL to download data from
    filename : str
        Name of the downloaded file
    out_dir : str, optional
        Output directory (default: data/raw)
    timeout : int, optional
        Request timeout in seconds

    Returns
    -------
    bool
        True if successful, False otherwise
    """

    os.makedirs(out_dir, exist_ok=True)
    outpath = os.path.join(out_dir, filename)

    try:
        response = requests.get(url, stream=True, timeout=timeout)
        response.raise_for_status()

        with open(outpath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive chunks
                    f.write(chunk)

        print(f"Downloaded '{filename}' successfully")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Download failed for '{filename}': {e}")
        return False