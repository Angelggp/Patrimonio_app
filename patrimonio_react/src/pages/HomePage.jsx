import Navbar from "../components/Navbar"
import AsideMenu from "../components/AsideMenu"

export default function HomePage() {


  return (
    <div className="min-h-screen bg-gray-50">
 
      <main className="max-w-5xl mx-auto px-4 py-8">
        <h1 className="text-2xl font-bold text-gray-900 mb-4">Bienvenido a Mi Sitio</h1>
        <p className="text-gray-600 mb-6">Un espacio minimalista para tu contenido.</p>
        
        {/* Contenido de ejemplo */}
        {[...Array(10)].map((_, i) => (
          <div key={i} className="bg-white rounded-lg shadow-sm p-4 mb-4">
            <h2 className="text-lg font-semibold mb-2">Sección {i + 1}</h2>
            <p className="text-gray-600 text-sm">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </p>
          </div>
        ))}
      </main>

      {/* Footer minimalista */}
      <footer className="bg-gray-100 text-gray-600 py-4 text-sm">
        <div className="max-w-5xl mx-auto px-4 text-center">
          &copy; 2023 Mi Sitio. Todos los derechos reservados.
        </div>
      </footer>
    </div>
  )
}