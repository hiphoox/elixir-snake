defmodule Snake.Worker do
  use GenServer

  #############
  # Public  API
  #############
  @doc """
  Starts snake worker.
  """
  def start_link(state) do
    GenServer.start_link(__MODULE__, state, [])
  end

  def validate do
    :poolboy.transaction(:snake_pool, fn(worker)-> :gen_server.call(worker,:validate) end)
  end

  ###################
  # Private Functions
  ###################
  @doc """
   Realiza la carga inicial de los schemas soportados del archivo de configuracion y
   genera una Keywordlist que contiene los eschemas soportados. Si no se puede cargar
   ningun schema, se manda el error para que el worker no pueda iniciar.
  """
  def init(state) do
    {:ok, pp} = :python.start([{:python_path, './lib/python_scripts'},{:python, 'python'}])
    :python.call(pp, :schema, :load_dpiva, [])
    {:ok, pp}
  end

  @doc """
   Llamada generica de un gen server, que atiende la peticion para validar contra schema un documento fiscal.
  """
  def handle_call(:validate, _from, pp) do
    {:ok, xml} = File.read("./dpiva_generado_oxygen.xml")
    IO.inspect :python.call(pp, :schema, :validate_dpiva, [xml])
    {:reply,:ok,pp}
  end

end
