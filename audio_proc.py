def audio_file(file_path)
        y, sr = librosa.load(file_path)
        

        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        rms = librosa.feature.rms(y=y)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)  
        

        features = np.concatenate([chroma_stft, rms, spectral_centroid, spectral_bandwidth,
                                   rolloff, zero_crossing_rate, mfccs[:9]], axis=0)
        return features
