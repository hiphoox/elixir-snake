defmodule Snake do
  use Application

  use Application

  def start(_type, _args) do
    Snake.Supervisor.start_link
  end
  # # See http://elixir-lang.org/docs/stable/elixir/Application.html
  # # for more information on OTP Applications
  # def start(_type, _args) do
  #   import Supervisor.Spec, warn: false

  #   children = [
  #     # Define workers and child supervisors to be supervised
  #     worker(Snake.Worker, []),
  #   ]

  #   # See http://elixir-lang.org/docs/stable/elixir/Supervisor.html
  #   # for other strategies and supported options
  #   opts = [strategy: :one_for_one, name: Snake.Supervisor]
  #   Supervisor.start_link(children, opts)
  # end

  # def a do
  #   {:ok, pp} = :python.start()
  #   :python.call(pp, :sys, String.to_atom("version.__str__"), [])
  # end

  # def b do
  #   name = IO.gets "What's your name?\n"
  #   name = String.strip(name)
  #   {:ok, pp} = :python.start([{:python_path, './lib/python_scripts'},{:python, 'python'}])
  #   :python.call(pp, :play, :func, [name])
  # end

  # def c do
  #   {:ok, pp} = :python.start([{:python_path, './lib/python_scripts'},{:python, 'python'}])
  #   :python.call(pp, :atoms, :pids, [])
  #   :python.call(pp, :atoms, :pids_more, [1000])
  # end

  # def d do
  #   {:ok, xml} = File.read("./dpiva_generado_oxygen.xml")
  #   {:ok, pp} = :python.start([{:python_path, './lib/python_scripts'},{:python, 'python'}])
  #   :python.call(pp, :play, :validate, [xml])
  # end

  # def e do
  #   {:ok, pp} = :python.start([{:python_path, './lib/python_scripts'},{:python, 'python'}])
  #   :python.call(pp, :play, :load_schema, [])
  # end

  # def valid_test(schema) do
  #   {:ok, pp} = :python.start([{:python_path, './lib/python_scripts'},{:python, 'python'}])
  #   {:ok, xml} = File.read("./dpiva_generado_oxygen.xml")
  #   :python.call(pp, :play, :validate_full, [xml,schema])
  # end

  # def testing_class()do
  #   {:ok, pp} = :python.start([{:python_path, './lib/python_scripts'},{:python, 'python'}])
  #   {:ok, xml} = File.read("./dpiva_generado_oxygen.xml")
  #   :python.call(pp, :schema, :validate_dpiva, [xml])
  # end

end
