// ------------------------------------------- //
//     TTS lib for Friday2.0 in rust           //
// ------------------------------------------- //

// use pyo3 to convert to python class
use pyo3::prelude::*;

// use tts_rust lib for text to speech conversion
use tts_rust::languages::Languages;
use tts_rust::tts::GTTSClient;

#[pyclass]
pub struct TextToSpeech {
    narrator: GTTSClient,
}

#[pymethods]
impl TextToSpeech {
    #[new]
    pub fn new(volume: f32) -> PyResult<Self> {
        Ok(TextToSpeech{
            narrator: GTTSClient {
                volume,
                language: Languages::English,
                tld: "com",
            }
        })
    }

    pub fn speak(&mut self, text: &str) -> PyResult<()> {

        let narrator = GTTSClient{
            volume: self.narrator.volume,
            language: self.narrator.language.clone(),
            tld: self.narrator.tld,
        };

        let new_text = text.to_string();

        let handle = std::thread::spawn(move || {
            narrator.speak(&new_text).unwrap();
        });

        handle.join().unwrap();

        Ok(())
    }

    pub fn save(&self, text: &str, path: &str) -> PyResult<()> {
        
        let narrator = GTTSClient {
            volume: self.narrator.volume,
            language: self.narrator.language.clone(),
            tld: self.narrator.tld,
        };

        let new_text = text.to_string();
        let new_path = path.to_string();

        let handle = std::thread::spawn(move || {
            narrator.save_to_file(&new_text, &new_path).unwrap();
        });

        handle.join().unwrap();

        Ok(())

    }
}

#[pymodule]
pub fn gtts(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<TextToSpeech>()?;
    Ok(())
}