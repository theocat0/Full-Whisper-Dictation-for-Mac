import SwiftUI
import AVFoundation

struct ContentView: View {
    @State private var isRecording = false
    @State private var transcript = "Press the button to start recording."
    @StateObject private var audioRecorder = AudioRecorder()

    var body: some View {
        VStack(spacing: 20) {
            Text(transcript)
                .padding()
            
            Button(isRecording ? "Stop Recording" : "Start Recording") {
                isRecording.toggle()
                if isRecording {
                    transcript = "Recording..."
                    audioRecorder.startRecording()
                } else {
                    audioRecorder.stopRecording { result in
                        switch result {
                        case .success(let url):
                            transcript = "Transcribing..."
                            transcribeAudio(url: url)
                        case .failure(let error):
                            transcript = "Recording failed: \(error.localizedDescription)"
                        }
                    }
                }
            }
        }
        .padding()
    }
    
    private func transcribeAudio(url: URL) {
        // This function should call Whisper's transcribing methods.
        // Here we mock the behavior for illustration.
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) { // Simulate some delay
            self.transcript = "Transcribed text appears here..."
        }
    }
}

class AudioRecorder: ObservableObject {
    private var audioRecorder: AVAudioRecorder?

    func startRecording() {
        let audioFilename = getDocumentsDirectory().appendingPathComponent("\(UUID().uuidString).m4a")
        
        let settings = [
            AVFormatIDKey: Int(kAudioFormatMPEG4AAC),
            AVSampleRateKey: 12000,
            AVNumberOfChannelsKey: 1,
            AVEncoderAudioQualityKey: AVAudioQuality.high.rawValue
        ]
        
        do {
            audioRecorder = try AVAudioRecorder(url: audioFilename, settings: settings)
            audioRecorder?.record()
        } catch {
            print("Failed to start recording: \(error)")
        }
    }
    
    func stopRecording(completion: @escaping (Result<URL, Error>) -> Void) {
        audioRecorder?.stop()
        if let url = audioRecorder?.url {
            completion(.success(url))
        } else {
            completion(.failure(RecordingError.recordingFailed))
        }
        audioRecorder = nil
    }
    
    private func getDocumentsDirectory() -> URL {
        FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
    }
    
    enum RecordingError: Error {
        case recordingFailed
    }
}

@main
struct WhisperApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
